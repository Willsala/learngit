# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-29 05:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_alltask4group'),
    ]

    operations = [
        migrations.CreateModel(
            name='task_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='username')),
                ('user_or_group', models.CharField(max_length=1, verbose_name='user_or_group')),
                ('project_loc', models.CharField(max_length=100, verbose_name='project_loc')),
                ('authority', models.CharField(max_length=20, verbose_name='authority')),
                ('request_serial_num', models.IntegerField(verbose_name='request_serial_num')),
                ('task_priority', models.IntegerField(default=0, verbose_name='task_priority')),
                ('ptn_name', models.CharField(max_length=30, verbose_name='ptn_file_name')),
                ('group', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Users.Group')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Users.Users')),
            ],
        ),
        migrations.CreateModel(
            name='user4serving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t', models.IntegerField(default=1, verbose_name='t')),
                ('x', models.IntegerField(verbose_name='x')),
                ('x_current', models.IntegerField(verbose_name='x_current')),
                ('w', models.FloatField(verbose_name='w')),
                ('group', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Users.Group')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Users.Users')),
            ],
        ),
        migrations.CreateModel(
            name='user_in_queue',
            fields=[
                ('x', models.IntegerField(verbose_name='x')),
                ('serial', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='serial')),
                ('group', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Users.Group')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Users.Users')),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='authority',
        ),
        migrations.RemoveField(
            model_name='task',
            name='task_priority',
        ),
    ]
