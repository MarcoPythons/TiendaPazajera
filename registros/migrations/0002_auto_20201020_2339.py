# Generated by Django 3.1.1 on 2020-10-21 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='contrasenia',
            field=models.CharField(max_length=8, verbose_name='Constraseña'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(verbose_name='Fecha de nacimiento'),
        ),
    ]
