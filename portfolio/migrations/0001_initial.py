# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Service'
        db.create_table('portafolio_service', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('portafolio', ['Service'])

        # Adding model 'Client'
        db.create_table('portafolio_client', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('portafolio', ['Client'])

        # Adding model 'Proyect'
        db.create_table('portafolio_proyect', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(related_name='proyectos', to=orm['portafolio.Service'])),
            ('country', self.gf('django_countries.fields.CountryField')(max_length=2)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(related_name='proyectos', to=orm['portafolio.Client'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description_short', self.gf('django.db.models.fields.TextField')()),
            ('description_long', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('portafolio', ['Proyect'])

        # Adding model 'Image'
        db.create_table('portafolio_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('proyect', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['portafolio.Proyect'])),
        ))
        db.send_create_signal('portafolio', ['Image'])

        # Adding model 'PortafolioPlugin'
        db.create_table('cmsplugin_portafolioplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('portafolio', ['PortafolioPlugin'])

        # Adding M2M table for field portafolio on 'PortafolioPlugin'
        db.create_table('portafolio_portafolioplugin_portafolio', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('portafolioplugin', models.ForeignKey(orm['portafolio.portafolioplugin'], null=False)),
            ('proyect', models.ForeignKey(orm['portafolio.proyect'], null=False))
        ))
        db.create_unique('portafolio_portafolioplugin_portafolio', ['portafolioplugin_id', 'proyect_id'])


    def backwards(self, orm):
        
        # Deleting model 'Service'
        db.delete_table('portafolio_service')

        # Deleting model 'Client'
        db.delete_table('portafolio_client')

        # Deleting model 'Proyect'
        db.delete_table('portafolio_proyect')

        # Deleting model 'Image'
        db.delete_table('portafolio_image')

        # Deleting model 'PortafolioPlugin'
        db.delete_table('cmsplugin_portafolioplugin')

        # Removing M2M table for field portafolio on 'PortafolioPlugin'
        db.delete_table('portafolio_portafolioplugin_portafolio')


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
        'portafolio.client': {
            'Meta': {'object_name': 'Client'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'portafolio.image': {
            'Meta': {'object_name': 'Image'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'proyect': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['portafolio.Proyect']"})
        },
        'portafolio.portafolioplugin': {
            'Meta': {'object_name': 'PortafolioPlugin', 'db_table': "'cmsplugin_portafolioplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'portafolio': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['portafolio.Proyect']", 'symmetrical': 'False'})
        },
        'portafolio.proyect': {
            'Meta': {'object_name': 'Proyect'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'proyectos'", 'to': "orm['portafolio.Client']"}),
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'description_long': ('django.db.models.fields.TextField', [], {}),
            'description_short': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'proyectos'", 'to': "orm['portafolio.Service']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'portafolio.service': {
            'Meta': {'object_name': 'Service'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['portafolio']
