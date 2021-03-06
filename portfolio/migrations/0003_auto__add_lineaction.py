# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'LineAction'
        db.create_table('portfolio_lineaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('portfolio', ['LineAction'])

        # Adding M2M table for field line_action on 'Proyect'
        db.create_table('portfolio_proyect_line_action', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proyect', models.ForeignKey(orm['portfolio.proyect'], null=False)),
            ('lineaction', models.ForeignKey(orm['portfolio.lineaction'], null=False))
        ))
        db.create_unique('portfolio_proyect_line_action', ['proyect_id', 'lineaction_id'])


    def backwards(self, orm):
        
        # Deleting model 'LineAction'
        db.delete_table('portfolio_lineaction')

        # Removing M2M table for field line_action on 'Proyect'
        db.delete_table('portfolio_proyect_line_action')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'portfolio.client': {
            'Meta': {'object_name': 'Client'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'portfolio.country': {
            'Meta': {'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'portfolio.image': {
            'Meta': {'ordering': "('sequence',)", 'object_name': 'Image'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'main': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'proyect': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['portfolio.Proyect']"}),
            'sequence': ('django.db.models.fields.IntegerField', [], {})
        },
        'portfolio.lineaction': {
            'Meta': {'object_name': 'LineAction'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'portfolio.portfolioplugin': {
            'Meta': {'object_name': 'PortfolioPlugin', 'db_table': "'cmsplugin_portfolioplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'portfolio': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['portfolio.Proyect']", 'symmetrical': 'False'})
        },
        'portfolio.proyect': {
            'Meta': {'object_name': 'Proyect'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'proyects'", 'to': "orm['portfolio.Client']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'proyects'", 'to': "orm['portfolio.Country']"}),
            'description_long': ('django.db.models.fields.TextField', [], {}),
            'description_short': ('django.db.models.fields.TextField', [], {}),
            'facebook_like': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line_action': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['portfolio.LineAction']", 'symmetrical': 'False'}),
            'main_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sequence': ('django.db.models.fields.IntegerField', [], {}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'proyects'", 'to': "orm['portfolio.Service']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'portfolio.service': {
            'Meta': {'object_name': 'Service'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['portfolio']
