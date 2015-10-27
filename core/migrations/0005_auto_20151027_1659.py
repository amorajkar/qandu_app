# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151027_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='question',
            field=models.ForeignKey(blank=True, to='core.Question', null=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
