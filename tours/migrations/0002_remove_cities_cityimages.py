# Generated by Django 5.0.6 on 2024-05-14 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cities',
            name='cityImages',
        ),
    ]
