import json

from django.core.management import BaseCommand

from catalog.models import Product, Category

file_json = 'catalog.json'

class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        # Здесь мы получаем данные из фикстурв с категориями
        with open(file_json, 'r', encoding='utf-8') as file:
            categories = file.read()

        return json.loads(categories)

    @staticmethod
    def json_read_products():
        # Здесь мы получаем данные из фикстурв с продуктами
        with open(file_json, 'r', encoding='utf-8') as file:
            products = file.read()

        return json.loads(products)

    def handle(self, *args, **options):
        # Удалите все продукты
        Product.objects.all().delete()
        # Удалите все категории
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            if category['model'] == 'catalog.category':
                category_for_create.append(
                    Category(id=category['pk'],
                            name=category["fields"]["name"],
                            description=category["fields"]["description"],
                             )
                )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            if product['model'] == 'catalog.product':
                product_for_create.append(
                    Product(pk=product["pk"],
                            name=product["fields"]["name"],
                            description=product["fields"]["description"],
                            purchase_price=product["fields"]["purchase_price"],
                            image=product["fields"]["image"],
                            category=Category.objects.get(pk=product["fields"]["category"]),
                            created_at=product["fields"]["created_at"],
                            updated_at=product["fields"]["updated_at"],
                            )
                )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
