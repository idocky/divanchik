# Generated by Django 4.1 on 2022-08-09 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_category_item_item_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cat_slug',
            field=models.SlugField(blank=True, max_length=15, null=True),
        ),
    ]
