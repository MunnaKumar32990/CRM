# Generated by Django 4.2.16 on 2024-11-30 09:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_customerinteraction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerinteraction',
            name='date',
            field=models.DateTimeField(default=datetime.timezone),
        ),
    ]
