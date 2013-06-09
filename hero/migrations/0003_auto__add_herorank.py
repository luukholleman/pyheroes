# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HeroRank'
        db.create_table(u'hero_herorank', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hero', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hero.Hero'])),
            ('ranklist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ranklist.Ranklist'])),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
            ('all_all', self.gf('django.db.models.fields.IntegerField')()),
            ('all_class', self.gf('django.db.models.fields.IntegerField')()),
            ('region_all', self.gf('django.db.models.fields.IntegerField')()),
            ('region_class', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'hero', ['HeroRank'])


    def backwards(self, orm):
        # Deleting model 'HeroRank'
        db.delete_table(u'hero_herorank')


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
        u'hero.herorank': {
            'Meta': {'object_name': 'HeroRank'},
            'all_all': ('django.db.models.fields.IntegerField', [], {}),
            'all_class': ('django.db.models.fields.IntegerField', [], {}),
            'hero': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hero.Hero']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ranklist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ranklist.Ranklist']"}),
            'region_all': ('django.db.models.fields.IntegerField', [], {}),
            'region_class': ('django.db.models.fields.IntegerField', [], {}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        u'klass.klass': {
            'Meta': {'object_name': 'Klass'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
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

    complete_apps = ['hero']