from django.db import models


# Создавайте свои модели здесь


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        max_length=1000, verbose_name="Описание", help_text="Введите описание продукта"
    )
    image = models.ImageField(
        upload_to="products/",
        verbose_name="Изображение продукта",
        help_text="Загрузите изображение продукта",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Категория",
        blank=True,
        related_name="Product",
    )
    purchase_price = models.IntegerField(
        null=True, blank=True, verbose_name="Цена за покупку", help_text="Введите цену"
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )

    def __str__(self):
        return (
            f"{self.name}{self.description}{self.category}{self.purchase_price}"
            f"{self.created_at}{self.updated_at}"
        )
    views_counter = models.PositiveIntegerField(
        verbose_name="Счёстчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category"]


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование категории",
        help_text="Введите название категории",
    )
    description = models.TextField(
        max_length=1000,
        verbose_name="Описание категории",
        help_text="Введите описание категории",
    )

    def __str__(self):
        return f"{self.name}{self.description}"

    class Meta:
        verbose_name = "Категорию продукта"
        verbose_name_plural = "Категории"
