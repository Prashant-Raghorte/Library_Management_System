# Generated by Django 3.2.16 on 2022-11-24 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0008_auto_20221124_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
        migrations.AddField(
            model_name='teacher',
            name='email_id',
            field=models.EmailField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]