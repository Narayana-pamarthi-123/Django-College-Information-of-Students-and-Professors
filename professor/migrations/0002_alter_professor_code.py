# Generated by Django 5.0.2 on 2024-02-29 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='Code',
            field=models.IntegerField(unique=True),
        ),
    ]
