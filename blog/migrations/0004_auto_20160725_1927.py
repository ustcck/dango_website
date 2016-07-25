# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_student_sex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
        migrations.AlterField(
            model_name='student',
            name='intime',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(related_name='student_teacher', default=1, to='blog.Teacher'),
            preserve_default=False,
        ),
    ]
