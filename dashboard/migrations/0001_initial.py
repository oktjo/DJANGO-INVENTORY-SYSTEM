# Generated by Django 5.0.6 on 2024-06-27 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Stationary', 'Stationary'), ('Electronics', 'Electronics'), ('Food', 'Food')], max_length=20)),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
    ]
