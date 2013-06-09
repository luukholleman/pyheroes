# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table(u'item_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hero', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hero.Hero'])),
            ('slot', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('color', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('tooltip', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'item', ['Item'])


    def backwards(self, orm):
        # Deleting model 'Item'
        db.delete_table(u'item_item')


    models = {
        u'career.career': {
            'Meta': {'object_name': 'Career'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_api_request': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'region': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        u'hero.hero': {
            'Meta': {'object_name': 'Hero'},
            'blizzard_id': ('django.db.models.fields.IntegerField', [], {}),
            'career': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['career.Career']"}),
            'gender': ('django.db.models.fields.SmallIntegerField', [], {}),
            'hardcore': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'klass': ('django.db.models.fields.SmallIntegerField', [], {}),
            'last_api_request': ('django.db.models.fields.DateTimeField', [], {}),
            'last_played': ('django.db.models.fields.DateTimeField', [], {}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'paragon_level': ('django.db.models.fields.IntegerField', [], {}),
            'region': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        u'item.item': {
            'Meta': {'object_name': 'Item'},
            'color': ('django.db.models.fields.SmallIntegerField', [], {}),
            'hero': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hero.Hero']"}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slot': ('django.db.models.fields.SmallIntegerField', [], {}),
            'tooltip': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['item']