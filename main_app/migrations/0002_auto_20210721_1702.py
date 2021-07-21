# Generated by Django 3.2.3 on 2021-07-21 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='vac_required',
        ),
        migrations.AddField(
            model_name='event',
            name='covid_protocol',
            field=models.CharField(choices=[('N', 'Nothing Specified'), ('V', 'Vaccination Required'), ('M', 'Maks Required Indoors'), ('VM', 'Vaccination and Masks Required Indoors')], default='N', max_length=3, verbose_name='Covid Protocol'),
        ),
    ]
