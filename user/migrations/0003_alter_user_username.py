# Generated by Django 5.0.4 on 2024-05-04 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, unique=True, verbose_name='username'),
        ),
    ]
