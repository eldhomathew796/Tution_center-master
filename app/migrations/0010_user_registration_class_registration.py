# Generated by Django 4.0.3 on 2022-03-30 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_designation_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_registration',
            name='class_registration',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='class_registration', to='app.class_registration'),
        ),
    ]
