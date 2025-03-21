from django.db import migrations

def insert_migrations(apps, schema_editor):
    Currency = apps.get_model('tradingbotweb', 'Currency')
    Currency(symbol='GBP', usd_value=1.4).save()
    Currency(symbol='EUR', usd_value=1.2).save()
    Currency(symbol='BRL', usd_value=0.2).save()
    Currency(symbol='BTC', usd_value=55000.0).save()
    Currency(symbol='ETH', usd_value=3000.0).save()

class Migration(migrations.Migration):

    dependencies = [
        ('tradingbotweb', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_migrations)
    ]