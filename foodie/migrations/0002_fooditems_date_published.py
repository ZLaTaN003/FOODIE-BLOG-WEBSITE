# Generated by Django 5.0.2 on 2024-03-02 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditems',
            name='date_published',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
