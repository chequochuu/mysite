# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_aaa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aaa',
            old_name='aquestion_text',
            new_name='question_text',
        ),
    ]
