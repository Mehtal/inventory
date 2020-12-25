# Generated by Django 3.1.4 on 2020-12-25 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='variant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.variant'),
            preserve_default=False,
        ),
    ]
