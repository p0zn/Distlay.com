# Generated by Django 3.2.9 on 2021-12-14 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20211213_2235'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
    ]