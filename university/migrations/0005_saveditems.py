# Generated by Django 4.0.6 on 2022-07-30 03:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('university', '0004_alter_university_program_abbreviation'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_page', models.CharField(max_length=100)),
                ('item_name', models.CharField(blank=True, default='GCU CS', max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
