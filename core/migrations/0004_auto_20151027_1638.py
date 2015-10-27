# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='question',
        ),
        migrations.AddField(
            model_name='vote',
            name='answer',
            field=models.ForeignKey(blank=True, to='core.Answer', null=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(blank=True, to='core.Question', null=True),
        ),
    ]
