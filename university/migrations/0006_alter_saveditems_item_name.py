# Generated by Django 4.0.6 on 2022-07-30 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0005_saveditems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saveditems',
            name='item_name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
