# Generated by Django 5.0.2 on 2024-03-25 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0011_alter_reviews_fooditem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='FoodItems',
            new_name='FoodItem',
        ),
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
    ]