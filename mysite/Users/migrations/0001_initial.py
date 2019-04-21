# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-14 15:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='au4group',
            fields=[
                ('group_id', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='group_id')),
                ('au4admin', models.CharField(default='10110', max_length=5, verbose_name='authority_of_admin')),
                ('au4pj_admin', models.CharField(default='10100', max_length=5, verbose_name='authority_of_pj_admin')),
            ],
        ),
        migrations.CreateModel(
            name='au4pj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pj_name', models.CharField(max_length=30, verbose_name='project_name')),
                ('user_au4pj', models.CharField(max_length=3, verbose_name='user_authority4pj')),
                ('tag', models.BooleanField(default=False, verbose_name='creator')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='group_id')),
                ('group_name', models.CharField(max_length=50, verbose_name='group_name')),
            ],
        ),
        migrations.CreateModel(
            name='Group_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authority', models.CharField(max_length=1, verbose_name='authority')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.IntegerField(verbose_name='group_id')),
                ('inviter_name', models.CharField(max_length=20, verbose_name='username')),
                ('invitee_au', models.CharField(max_length=1, verbose_name='authority')),
                ('notes', models.CharField(max_length=100, verbose_name='notes')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('username', models.CharField(max_length=20, verbose_name='project_loc')),
                ('tag', models.CharField(max_length=1, verbose_name='user_or_group')),
                ('project_loc', models.CharField(max_length=100, verbose_name='project_loc')),
                ('authority', models.CharField(max_length=20, verbose_name='authority')),
                ('request_serial_num', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='request_serial_num')),
                ('task_priority', models.IntegerField(verbose_name='task_priority')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='username')),
                ('password', models.CharField(max_length=20, verbose_name='password')),
                ('authority', models.CharField(default='common_user', max_length=20, verbose_name='authority')),
                ('email', models.CharField(max_length=50, null=True, verbose_name='email')),
                ('subscribe', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='invitation',
            name='invitee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.Users'),
        ),
        migrations.AddField(
            model_name='group_item',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.Users'),
        ),
        migrations.AddField(
            model_name='au4pj',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.Group'),
        ),
        migrations.AddField(
            model_name='au4pj',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.Users'),
        ),
    ]
