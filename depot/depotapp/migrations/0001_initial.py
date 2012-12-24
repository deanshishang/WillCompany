# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product'
        db.create_table('depotapp_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('imag_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('date_available', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('depotapp', ['Product'])

        # Adding model 'Order'
        db.create_table('depotapp_order', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('depotapp', ['Order'])

        # Adding model 'LineItem'
        db.create_table('depotapp_lineitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['depotapp.Product'])),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['depotapp.Order'])),
            ('unit_price', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('depotapp', ['LineItem'])


    def backwards(self, orm):
        # Deleting model 'Product'
        db.delete_table('depotapp_product')

        # Deleting model 'Order'
        db.delete_table('depotapp_order')

        # Deleting model 'LineItem'
        db.delete_table('depotapp_lineitem')


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