# Generated by Django 5.0.2 on 2024-02-29 19:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0016_alter_student_date_of_joining'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Date_of_joining',
            field=models.DateField(default=datetime.datetime(2024, 3, 1, 0, 47, 2, 468531)),
        ),
    ]
