# Generated by Django 5.1.7 on 2025-03-14 08:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradingbotweb', '0003_currencyhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('share_portfolio', models.IntegerField(default=0)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tradingbotweb.currency')),
            ],
        ),
    ]
