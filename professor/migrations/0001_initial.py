# Generated by Django 5.0.2 on 2024-02-29 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=3, unique=True)),
                ('Professor_name', models.CharField(max_length=100)),
                ('Subject_name', models.CharField(max_length=10)),
                ('Age', models.IntegerField(blank=True, null=True)),
                ('Contact', models.CharField(max_length=10)),
            ],
        ),
    ]
