# Generated by Django 3.0 on 2020-04-21 22:25

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='name')),
                ('family', models.CharField(max_length=32, verbose_name='family')),
                ('patronymic', models.CharField(blank=True, max_length=32, verbose_name='patronymic')),
                ('age', models.DateTimeField()),
                ('login', models.CharField(max_length=32, unique=True, verbose_name='login')),
                ('password', models.CharField(max_length=32, verbose_name='password')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default='803397173', max_length=32, unique=True, verbose_name='name')),
                ('balance', models.IntegerField(default=0)),
                ('date_open', models.DateTimeField(default=datetime.datetime(2020, 4, 21, 22, 25, 19, 525073, tzinfo=utc))),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal_area.Client')),
            ],
        ),
    ]