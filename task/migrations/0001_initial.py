# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Task'
        db.create_table(u'task_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('region', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('battletag', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('hero_id', self.gf('django.db.models.fields.IntegerField')()),
            ('item_id', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('started', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ended', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'task', ['Task'])


    def backwards(self, orm):
        # Deleting model 'Task'
        db.delete_table(u'task_task')


    models = {
        u'task.task': {
            'Meta': {'object_name': 'Task'},
            'battletag': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ended': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hero_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'region': ('django.db.models.fields.SmallIntegerField', [], {}),
            'started': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.SmallIntegerField', [], {})
        }
    }

    complete_apps = ['task']