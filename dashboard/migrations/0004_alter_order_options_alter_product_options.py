# Generated by Django 5.0.6 on 2024-06-28 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Order'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Product'},
        ),
    ]
