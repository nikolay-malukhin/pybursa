# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('students', '0001_initial'),
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
                ('favourite_color', models.CharField(default=b'r', max_length=1, blank=True, choices=[(b'r', b'red'), (b'o', b'orange'), (b'y', b'yellow'), (b'g', b'green'), (b'b', b'blue')])),
                ('address', models.ForeignKey(blank=True, to='students.Address', null=True)),
                ('unliked_courses', models.ManyToManyField(to='courses.Course', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='student',
            name='dossier',
            field=models.OneToOneField(null=True, blank=True, to='students.Dossier'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='courses.Course', null=True, blank=True),
            preserve_default=True,
        ),
    ]
