# Generated by Django 3.1.1 on 2020-11-03 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0009_auto_20201103_0428'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='tipo_prenda',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
