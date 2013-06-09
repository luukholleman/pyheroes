# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Hero'
        db.create_table(u'hero_hero', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('career', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['career.Career'])),
            ('blizzard_id', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('hardcore', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
            ('paragon_level', self.gf('django.db.models.fields.IntegerField')()),
            ('gender', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('klass', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('last_played', self.gf('django.db.models.fields.DateTimeField')()),
            ('region', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('last_api_request', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'hero', ['Hero'])


    def backwards(self, orm):
        # Deleting model 'Hero'
        db.delete_table(u'hero_hero')


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
        }
    }

    complete_apps = ['hero']