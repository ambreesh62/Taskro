# Generated by Django 5.0.4 on 2024-05-04 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Location'),
        ),
    ]
