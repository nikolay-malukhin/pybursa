# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20141209_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(default=b'None'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='technology',
            field=models.CharField(max_length=255, choices=[(b'p', b'Python'), (b'r', b'Ruby'), (b'j', b'JS')]),
            preserve_default=True,
        ),
    ]
