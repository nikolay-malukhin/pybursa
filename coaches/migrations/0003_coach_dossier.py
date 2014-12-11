# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20141209_1300'),
        ('coaches', '0002_auto_20141209_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='dossier',
            field=models.OneToOneField(null=True, blank=True, to='students.Dossier'),
            preserve_default=True,
        ),
    ]
