# Generated by Django 4.2.4 on 2023-09-13 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peerchat', '0003_chatresponse'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatresponse',
            name='is_stressed',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
