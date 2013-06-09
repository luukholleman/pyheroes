# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Klass'
        db.create_table(u'klass_klass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'klass', ['Klass'])


    def backwards(self, orm):
        # Deleting model 'Klass'
        db.delete_table(u'klass_klass')


    models = {
        u'klass.klass': {
            'Meta': {'object_name': 'Klass'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['klass']