# Generated by Django 3.2.6 on 2022-04-02 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_covidgooglenewscontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='CovidMalaysiakiniContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=300)),
                ('url', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='HiringContent',
        ),
    ]
