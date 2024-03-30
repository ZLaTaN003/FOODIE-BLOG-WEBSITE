# Generated by Django 5.0.2 on 2024-03-13 12:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0007_alter_fooditems_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=80)),
                ('fooditem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodie.fooditems')),
            ],
        ),
    ]