# Generated by Django 4.1.3 on 2024-03-25 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='menu_item_description',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
