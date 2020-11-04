# Generated by Django 3.1.2 on 2020-11-03 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_auto_20201103_2151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_menus', to='restaurants.restaurant')),
            ],
        ),
    ]
