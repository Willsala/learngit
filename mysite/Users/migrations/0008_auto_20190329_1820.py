# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-29 10:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_auto_20190329_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_db',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.Group'),
        ),
        migrations.AlterField(
            model_name='task_db',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.Users'),
        ),
        migrations.AlterField(
            model_name='user4serving',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.Group'),
        ),
        migrations.AlterField(
            model_name='user4serving',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.Users'),
        ),
        migrations.AlterField(
            model_name='user_in_queue',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.Group'),
        ),
        migrations.AlterField(
            model_name='user_in_queue',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.Users'),
        ),
    ]