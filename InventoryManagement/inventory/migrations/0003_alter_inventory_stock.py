# Generated by Django 3.2.6 on 2022-04-06 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20220406_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
