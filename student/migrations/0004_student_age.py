# Generated by Django 5.0.2 on 2024-02-28 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_student_branch_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
