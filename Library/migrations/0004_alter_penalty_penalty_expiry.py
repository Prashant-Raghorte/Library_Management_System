# Generated by Django 3.2.16 on 2022-11-21 10:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0003_auto_20221121_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penalty',
            name='penalty_expiry',
            field=models.DateField(verbose_name=datetime.datetime(2022, 12, 21, 16, 0, 40, 905034)),
        ),
    ]
