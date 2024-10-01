from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name", "category"],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.RenameField(
            model_name="category",
            old_name="Description",
            new_name="description",
        ),
        migrations.RenameField(
            model_name="category",
            old_name="Name",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="Category",
            new_name="category",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="Description",
            new_name="description",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="Image",
            new_name="image",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="Name",
            new_name="name",
        ),
        migrations.RemoveField(
            model_name="product",
            name="Purchase_price",
        ),
        migrations.AddField(
            model_name="product",
            name="purchase_price",
            field=models.IntegerField(
                blank=True,
                help_text="Введите цену",
                null=True,
                verbose_name="Цена за покупку",
            ),
        ),
    ]
