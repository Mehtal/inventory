# Generated by Django 3.1.4 on 2020-12-25 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20201225_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_delivery',
            field=models.BooleanField(default=False, verbose_name='delivery status'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_seller',
            field=models.BooleanField(default=False, verbose_name='seller status'),
        ),
    ]