# Generated by Django 4.0.6 on 2022-08-02 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='field_of_interest',
            field=models.CharField(choices=[('SE', 'SE'), ('IT', 'IT'), ('CE', 'CE'), ('CS', 'CS'), ('A', 'A'), ('AED', 'AED'), ('CRP', 'CRP'), ('EER', 'EER'), ('CE', 'CE'), ('IME', 'IME'), ('ME', 'ME'), ('MCE', 'MCE'), ('MINE', 'MINE'), ('MME', 'MME'), ('PGE', 'PGE'), ('PID', 'PID'), ('PPE', 'PPE'), ('TEM', 'TEM'), ('CHE', 'CHE'), ('WRE', 'WRE')], default='None', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='university_name',
            field=models.CharField(choices=[('University of Engineering and Technology', 'University of Engineering and Technology'), ('Government College University Lahore', 'Government College University Lahore'), ('Lahore College for Women University', 'Lahore College for Women University'), ('Information Technology University', 'Information Technology University'), ('Kinnard College For Women University', 'Kinnard College For Women University'), ('University of Education', 'University of Education'), ('University of Punjab', 'University of Punjab')], default='None', max_length=50),
        ),
    ]
