# Generated by Django 2.2.8 on 2019-12-25 21:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SriTipoComprobante',
            fields=[
                ('sri_tipo_comprobante_id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('activo', models.BooleanField(default=True)),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('descripcion', models.CharField(max_length=50, unique=True)),
                ('alias', models.CharField(max_length=5, unique=True)),
                ('usuario_creador', models.ForeignKey(blank=True, null=True,
                                                      on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
