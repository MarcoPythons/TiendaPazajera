# Generated by Django 3.1.1 on 2020-10-27 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0003_auto_20201021_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
