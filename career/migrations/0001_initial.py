# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Career'
        db.create_table(u'career_career', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('region', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('last_api_request', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'career', ['Career'])


    def backwards(self, orm):
        # Deleting model 'Career'
        db.delete_table(u'career_career')


    models = {
        u'career.career': {
            'Meta': {'object_name': 'Career'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_api_request': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'region': ('django.db.models.fields.SmallIntegerField', [], {})
        }
    }

    complete_apps = ['career']