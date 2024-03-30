# Generated by Django 5.0.2 on 2024-03-26 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0012_rename_comments_comment_rename_fooditems_fooditem_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='fooditem',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='fooditem',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='image_url',
            field=models.CharField(default='nothing', max_length=2000),
        ),
    ]