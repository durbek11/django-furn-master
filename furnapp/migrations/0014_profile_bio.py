# Generated by Django 4.0.6 on 2022-08-17 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnapp', '0013_rename_user_profile_custom_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, default='bio', max_length=100),
        ),
    ]
