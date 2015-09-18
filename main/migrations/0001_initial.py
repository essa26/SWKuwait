# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=255)),
                ('clinic', models.ForeignKey(to='main.Clinic')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blood_sugar', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('comment', models.TextField(null=True)),
                ('level', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=15)),
                ('emergency1', models.CharField(max_length=15)),
                ('emergency2', models.CharField(max_length=15)),
                ('clinic', models.ForeignKey(to='main.Clinic')),
                ('doctor', models.ForeignKey(to='main.DoctorProfile')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='log',
            name='userprof',
            field=models.ForeignKey(to='main.UserProfile'),
        ),
    ]
