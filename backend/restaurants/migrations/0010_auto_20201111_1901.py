# Generated by Django 3.1.2 on 2020-11-11 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0009_auto_20201105_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='restaurant',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contact', to='restaurants.restaurant'),
        ),
        migrations.AlterField(
            model_name='coordinates',
            name='contact',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='coordinates', to='restaurants.contact'),
        ),
    ]
