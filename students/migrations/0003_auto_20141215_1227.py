# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20141209_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dossier',
            name='favourite_color',
            field=models.CharField(default=b'r', max_length=1, blank=True, choices=[(b'r', b'Red'), (b'o', b'Orange'), (b'y', b'Yellow'), (b'g', b'Green'), (b'l', b'Light Blue'), (b'b', b'Blue'), (b'v', b'Violet')]),
            preserve_default=True,
        ),
    ]
