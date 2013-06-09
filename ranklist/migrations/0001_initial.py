# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'ranklist_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'ranklist', ['Category'])

        # Adding model 'Ranklist'
        db.create_table(u'ranklist_ranklist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ranklist.Category'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('stat', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'ranklist', ['Ranklist'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'ranklist_category')

        # Deleting model 'Ranklist'
        db.delete_table(u'ranklist_ranklist')


    models = {
        u'ranklist.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'ranklist.ranklist': {
            'Meta': {'object_name': 'Ranklist'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ranklist.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'stat': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['ranklist']