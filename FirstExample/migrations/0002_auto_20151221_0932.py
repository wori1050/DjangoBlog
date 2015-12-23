# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FirstExample', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='filtered_image_file',
            field=models.ImageField(upload_to=b'static_files/uploaded/%Y/%m/%d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='image_file',
            field=models.ImageField(upload_to=b'static_file/uploaded/%Y/%m/%d'),
            preserve_default=True,
        ),
    ]
