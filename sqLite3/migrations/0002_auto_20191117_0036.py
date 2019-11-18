# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-11-16 16:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sqLite3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorname', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sqLite3.Author'),
        ),
    ]