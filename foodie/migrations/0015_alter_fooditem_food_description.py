# Generated by Django 5.0.2 on 2024-03-29 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0014_rename_category_categorylist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='food_description',
            field=models.CharField(max_length=2000),
        ),
    ]
