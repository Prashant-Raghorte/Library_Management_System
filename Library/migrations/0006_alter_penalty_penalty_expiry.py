# Generated by Django 3.2.16 on 2022-11-23 10:51

import Library.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0005_alter_penalty_penalty_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penalty',
            name='penalty_expiry',
            field=models.DateTimeField(default=Library.models.penalty_expiry_calculation),
        ),
    ]