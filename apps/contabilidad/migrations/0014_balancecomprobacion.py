# Generated by Django 2.2.8 on 2019-12-26 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0013_balancecomprobacion_query'),
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceComprobacion',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('saldo_deudor', models.DecimalField(decimal_places=5, default=0, max_digits=15)),
                ('saldo_acreedor', models.DecimalField(decimal_places=5, default=0, max_digits=15)),
            ],
            options={
                'db_table': 'contabilidad_balancecomprobacion',
                'managed': False,
            },
        ),
    ]
