# Generated by Django 4.0.3 on 2022-04-22 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_user_registration_dateofappointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='acntspayslip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_salary', models.IntegerField()),
                ('eno', models.CharField(max_length=100)),
                ('hra', models.IntegerField()),
                ('conveyns', models.CharField(max_length=100)),
                ('tax', models.IntegerField()),
                ('incentives', models.IntegerField()),
                ('fromdate', models.DateField(blank=True, null=True)),
                ('todate', models.DateField(blank=True, null=True)),
                ('taxengine', models.CharField(max_length=100)),
                ('incometax', models.IntegerField()),
                ('uan', models.CharField(max_length=100)),
                ('pf', models.IntegerField()),
                ('esi', models.CharField(max_length=100)),
                ('pro', models.CharField(max_length=100)),
                ('leavesno', models.IntegerField()),
                ('pf_tax', models.IntegerField()),
                ('delay', models.IntegerField()),
                ('basictype', models.CharField(default='', max_length=255)),
                ('hratype', models.CharField(default='', max_length=255)),
                ('contype', models.CharField(default='', max_length=255)),
                ('protype', models.CharField(default='', max_length=255)),
                ('instype', models.CharField(default='', max_length=255)),
                ('deltype', models.CharField(default='', max_length=255)),
                ('leatype', models.CharField(default='', max_length=255)),
                ('pftype', models.CharField(default='', max_length=255)),
                ('esitype', models.CharField(default='', max_length=255)),
                ('batch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='accbatch', to='app.batch')),
                ('designation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='desic', to='app.designation')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to='app.user_registration')),
            ],
        ),
    ]
