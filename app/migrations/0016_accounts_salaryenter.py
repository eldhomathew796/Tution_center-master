# Generated by Django 4.0.6 on 2022-07-14 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_accounts_dateofressigning'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='salaryenter',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
