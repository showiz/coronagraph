# Generated by Django 2.2.2 on 2020-04-01 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200329_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewCases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cases', models.IntegerField(verbose_name='Cant. Nuevos casos')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Última actualización')),
            ],
        ),
    ]
