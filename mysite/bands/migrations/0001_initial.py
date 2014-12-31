# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('can_rock', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'bands',
                'ordering': ['name'],
                'verbose_name': 'band',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name="Member's name")),
                ('instrument', models.CharField(choices=[('g', 'Guitar'), ('b', 'Bass'), ('d', 'Drums'), ('v', 'Vocal'), ('p', 'Piano')], max_length=1)),
                ('band', models.ForeignKey(related_name='band', to='bands.Band')),
            ],
            options={
                'verbose_name_plural': 'members',
                'ordering': ['name'],
                'verbose_name': 'member',
            },
            bases=(models.Model,),
        ),
    ]
