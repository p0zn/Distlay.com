# Generated by Django 3.2.9 on 2021-12-14 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20211214_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=None, max_length=100, null=True, unique=True),
        ),
    ]
