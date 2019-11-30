# Generated by Django 2.2.5 on 2019-10-08 19:42

from django.db import migrations, models
import hrm.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_seeker_id', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('ranking', models.FloatField()),
                ('resume', models.ImageField(blank=True, null=True, upload_to=hrm.models.Users.upload_resume)),
            ],
        ),
    ]