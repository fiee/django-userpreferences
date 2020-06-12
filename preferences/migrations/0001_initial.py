# -*- coding: utf-8 -*-
from django.db import models, migrations
from django.conf import settings
import preferences.fields
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPreferences',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('preferences', picklefield.fields.PickledObjectField(default={}, editable=False)),
                ('user', preferences.fields.AutoOneToOneField(related_name='preferences', null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
