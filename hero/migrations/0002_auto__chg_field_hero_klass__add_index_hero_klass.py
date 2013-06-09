# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'Hero.klass' to match new field type.
        db.rename_column(u'hero_hero', 'klass', 'klass_id')
        # Changing field 'Hero.klass'
        db.alter_column(u'hero_hero', 'klass_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['klass.Klass']))
        # Adding index on 'Hero', fields ['klass']
        db.create_index(u'hero_hero', ['klass_id'])


    def backwards(self, orm):
        # Removing index on 'Hero', fields ['klass']
        db.delete_index(u'hero_hero', ['klass_id'])


        # Renaming column for 'Hero.klass' to match new field type.
        db.rename_column(u'hero_hero', 'klass_id', 'klass')
        # Changing field 'Hero.klass'
        db.alter_column(u'hero_hero', 'klass', self.gf('django.db.models.fields.SmallIntegerField')())

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
            'klass': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['klass.Klass']"}),
            'last_api_request': ('django.db.models.fields.DateTimeField', [], {}),
            'last_played': ('django.db.models.fields.DateTimeField', [], {}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'paragon_level': ('django.db.models.fields.IntegerField', [], {}),
            'region': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        u'klass.klass': {
            'Meta': {'object_name': 'Klass'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['hero']