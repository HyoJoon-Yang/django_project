# Generated by Django 4.1.6 on 2023-02-16 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_category_post_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("tagName", models.CharField(max_length=30, unique=True)),
                (
                    "slug",
                    models.SlugField(allow_unicode=True, max_length=30, unique=True),
                ),
            ],
        ),
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "categories"},
        ),
        migrations.AddField(
            model_name="post",
            name="tag",
            field=models.ManyToManyField(blank=True, to="blog.tag"),
        ),
    ]
