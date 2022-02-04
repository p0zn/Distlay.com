# Generated by Django 3.2.9 on 2022-01-03 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0008_questions_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=255, verbose_name='Select reason for reporting')),
                ('message', models.CharField(max_length=255)),
            ],
        ),
    ]