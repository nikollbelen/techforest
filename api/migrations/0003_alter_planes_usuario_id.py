# Generated by Django 3.2.9 on 2021-12-04 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211204_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planes',
            name='usuario_id',
            field=models.OneToOneField(default='0', on_delete=django.db.models.deletion.CASCADE, to='api.usuarios'),
        ),
    ]
