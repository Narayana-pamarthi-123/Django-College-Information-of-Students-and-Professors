# Generated by Django 5.0.2 on 2024-02-28 08:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_student_date_of_joining'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Date_of_joining',
            field=models.DateField(default=datetime.datetime(2024, 2, 28, 14, 24, 11, 586433)),
        ),
    ]
