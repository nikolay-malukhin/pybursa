# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zip', models.CharField(max_length=5)),
                ('country', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=255, blank=True)),
                ('city', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255, blank=True)),
                ('street', models.CharField(max_length=255)),
                ('house', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('favourite_color', models.CharField(default=b'r', max_length=1, blank=True, choices=[(b'r', b'Red'), (b'o', b'Orange'), (b'y', b'Yellow'), (b'g', b'Green'), (b'l', b'Light Blue'), (b'b', b'Blue'), (b'v', b'Violet')])),
                ('address', models.ForeignKey(blank=True, to='students.Address', null=True)),
                ('unliked_courses', models.ManyToManyField(to='courses.Course', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=75)),
                ('phone_number', models.CharField(max_length=13, blank=True)),
                ('package', models.CharField(default=b's', max_length=1, choices=[(b's', b'Standard'), (b'g', b'Gold'), (b'p', b'Platinum')])),
                ('courses', models.ManyToManyField(to='courses.Course', null=True, blank=True)),
                ('dossier', models.OneToOneField(null=True, blank=True, to='students.Dossier')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
