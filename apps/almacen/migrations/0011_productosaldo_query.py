# Generated by Django 2.2.8 on 2019-12-26 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0010_inventarioexistencia'),
    ]

    operations = [
        migrations.RunSQL("""
            CREATE OR REPLACE VIEW almacen_productosaldo AS
            SELECT row_number() OVER () as id,
                prod.producto_id,
                und.unidad_medida_id,
                prod_saldo.cantidad AS existencia
            FROM producto_producto prod
            LEFT JOIN unidadmedida_unidadmedida und ON und.unidad_medida_id = prod.unidad_principal_id
            LEFT JOIN almacen_movimientosaldo prod_saldo ON prod_saldo.producto_id = prod.producto_id
            ORDER BY prod.nombre;
        """),
    ]
