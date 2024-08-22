# Generated by Django 4.2.13 on 2024-08-22 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Укажите название категории",
                        max_length=100,
                        verbose_name="Наименование категории",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Опишите категории",
                        null=True,
                        verbose_name="Описание категории",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Укажите название продукта",
                        max_length=100,
                        verbose_name="Наименование продукта",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Опишите продукт",
                        null=True,
                        verbose_name="Описание продукта",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите фото продукта",
                        null=True,
                        upload_to="catalog/photo",
                        verbose_name="Фото",
                    ),
                ),
                (
                    "price_pay",
                    models.IntegerField(
                        blank=True,
                        help_text="Введите цену",
                        null=True,
                        verbose_name="Цена за покупку",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        help_text="Введите дату", verbose_name="Дата создания записи"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        help_text="Введите дату", verbose_name="Дата изменения записи"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="category",
                        to="catalog.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ["name", "price_pay"],
            },
        ),
    ]
