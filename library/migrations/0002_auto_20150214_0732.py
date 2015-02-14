# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, upload_to=library.models.image_upload_path, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(to='library.Author', to_field='id'),
        ),
    ]
