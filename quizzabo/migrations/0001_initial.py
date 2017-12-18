# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('description', models.CharField(max_length='30', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('type', models.CharField(default='FREE', max_length=20, choices=[('FREE', 'FREE'), ('EASY', 'EASY'), ('MEDIUM', 'MEDIUM'), ('EXPERT', 'EXPERT')])),
                ('price', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Prices',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='pricing',
            field=models.ForeignKey(to='quizzabo.Pricing'),
        ),
    ]
