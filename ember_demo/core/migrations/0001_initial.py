# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product'
        db.create_table(u'core_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=2, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('isOnSale', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('product_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'core', ['Product'])

        # Adding model 'Review'
        db.create_table(u'core_review', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reviews', to=orm['core.Product'])),
        ))
        db.send_create_signal(u'core', ['Review'])


    def backwards(self, orm):
        # Deleting model 'Product'
        db.delete_table(u'core_product')

        # Deleting model 'Review'
        db.delete_table(u'core_review')


    models = {
        u'core.product': {
            'Meta': {'object_name': 'Product'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isOnSale': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2', 'blank': 'True'}),
            'product_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.review': {
            'Meta': {'object_name': 'Review'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reviews'", 'to': u"orm['core.Product']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['core']