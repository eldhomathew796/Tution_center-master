# Generated by Django 4.0.3 on 2022-03-30 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_user_registration_class_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_registration',
            name='dateofappointment',
            field=models.DateField(blank=True, null=True),
        ),
    ]
