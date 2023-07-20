# Generated by Django 2.2.8 on 2020-02-07 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0004_secuencia'),
        ('proveedor', '0004_proveedorresumen'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    to='administracion.Empresa')
        ),
    ]
