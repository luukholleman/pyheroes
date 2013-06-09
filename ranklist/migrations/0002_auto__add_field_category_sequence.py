# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Category.sequence'
        db.add_column(u'ranklist_category', 'sequence',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Category.sequence'
        db.delete_column(u'ranklist_category', 'sequence')


    models = {
        u'ranklist.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'sequence': ('django.db.models.fields.SmallIntegerField', [], {})
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