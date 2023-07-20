# Generated by Django 2.2.8 on 2019-12-26 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0012_productosaldo'),
    ]

    operations = [
        migrations.RunSQL("DROP VIEW IF EXISTS almacen_productoconsolidado;"),
        migrations.RunSQL("""
            CREATE OR REPLACE VIEW almacen_productoconsolidado AS
            SELECT row_number() OVER () as id,
                prod.producto_id,
                COALESCE(inv_entrada.cantidad, 0) AS entradas,
                COALESCE(inv_salida.cantidad,0) AS salidas,
                (COALESCE(inv_entrada.cantidad, 0)
                - COALESCE(inv_salida.cantidad,0)) AS saldo,
                prod.unidad_principal_id
            FROM producto_producto prod
            LEFT JOIN almacen_movimientoentrada inv_entrada ON inv_entrada.producto_id = prod.producto_id
            LEFT JOIN almacen_movimientosalida inv_salida ON inv_salida.producto_id = prod.producto_id;
        """),
    ]
