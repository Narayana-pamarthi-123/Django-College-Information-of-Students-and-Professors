# Generated by Django 5.0.2 on 2024-02-29 11:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_alter_student_age_alter_student_date_of_joining'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Date_of_joining',
            field=models.DateField(default=datetime.datetime(2024, 2, 29, 16, 53, 26, 252039)),
        ),
        migrations.AlterField(
            model_name='student',
            name='Roll_number',
            field=models.IntegerField(unique=True),
        ),
    ]
