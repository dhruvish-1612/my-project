# Generated by Django 4.1 on 2022-08-30 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.CharField(default='', max_length=100),
        ),
    ]
