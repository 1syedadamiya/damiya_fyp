# Generated by Django 4.0.6 on 2022-07-23 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='Male', max_length=15),
        ),
    ]
