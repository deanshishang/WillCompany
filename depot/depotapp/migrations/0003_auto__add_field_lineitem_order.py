# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'LineItem.order'
        db.add_column('depotapp_lineitem', 'order',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['depotapp.Order']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'LineItem.order'
        db.delete_column('depotapp_lineitem', 'order_id')


    models = {
        'depotapp.lineitem': {
            'Meta': {'object_name': 'LineItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['depotapp.Order']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['depotapp.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'})
        },
        'depotapp.order': {
            'Meta': {'object_name': 'Order'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'depotapp.product': {
            'Meta': {'object_name': 'Product'},
            'date_available': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imag_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['depotapp']