# Generated by Django 5.1.7 on 2025-03-14 08:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradingbotweb', '0004_currencybalance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencybalance',
            name='share_portfolio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
    ]
