# Generated by Django 2.2.2 on 2020-03-29 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200329_1410'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='regions',
            options={'ordering': ('infected',)},
        ),
        migrations.AlterField(
            model_name='regions',
            name='infected',
            field=models.IntegerField(max_length=254, verbose_name='Cant. Infectados'),
        ),
    ]
