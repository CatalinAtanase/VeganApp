# Generated by Django 3.1.2 on 2020-11-03 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20201103_2022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coordinates',
            options={'verbose_name': 'Coordinates', 'verbose_name_plural': 'Coordinates'},
        ),
    ]