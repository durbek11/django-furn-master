# Generated by Django 4.0.4 on 2022-08-03 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
