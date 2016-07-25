# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160725_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='sex',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
