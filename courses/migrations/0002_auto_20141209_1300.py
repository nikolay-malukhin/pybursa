# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20141209_1300'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='venue',
            field=models.ForeignKey(blank=True, to='students.Address', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='assistant',
            field=models.ForeignKey(related_name='assistant', blank=True, to='coaches.Coach', null=True),
            preserve_default=True,
        ),
    ]
