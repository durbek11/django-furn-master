# Generated by Django 4.0.6 on 2022-08-31 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnapp', '0035_alter_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.CharField(max_length=200),
        ),
    ]
