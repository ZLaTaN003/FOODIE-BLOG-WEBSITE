# Generated by Django 5.0.2 on 2024-03-25 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0010_alter_reviews_fooditem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='fooditem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodie.fooditems'),
        ),
    ]
