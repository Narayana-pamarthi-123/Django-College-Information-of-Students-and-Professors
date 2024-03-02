# Generated by Django 5.0.2 on 2024-02-29 11:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_alter_student_date_of_joining'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Age',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Date_of_joining',
            field=models.DateField(default=datetime.datetime(2024, 2, 29, 16, 50, 48, 600515)),
        ),
    ]