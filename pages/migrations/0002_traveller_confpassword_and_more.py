# Generated by Django 5.0.6 on 2024-05-13 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='traveller',
            name='Confpassword',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='traveller',
            name='favouritecities',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='traveller',
            name='visitedCities',
            field=models.CharField(max_length=40, null=True),
        ),
    ]