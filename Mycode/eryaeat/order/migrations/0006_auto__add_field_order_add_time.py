# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Order.add_time'
        db.add_column('order_order', 'add_time',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2012, 12, 24, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Order.add_time'
        db.delete_column('order_order', 'add_time')


    models = {
        'order.depot': {
            'Meta': {'object_name': 'Depot'},
            'add_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': "orm['order.Order']"})
        },
        'order.detail': {
            'Meta': {'object_name': 'Detail'},
            'add_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'depot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.Depot']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.Recipe']"})
        },
        'order.order': {
            'Meta': {'object_name': 'Order'},
            'add_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'orderno': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'recipe': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['order.Recipe']", 'symmetrical': 'False'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'table': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': "orm['order.Table']"})
        },
        'order.phoneid': {
            'Meta': {'object_name': 'Phoneid'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'table': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.Table']"})
        },
        'order.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'comments': ('django.db.models.fields.FloatField', [], {'default': '4'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'discount': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imgurl': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'rstatus': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'rtype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.Rtype']"}),
            'shelfdate': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'order.rtype': {
            'Meta': {'object_name': 'Rtype'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'sequence': ('django.db.models.fields.IntegerField', [], {'default': '9'})
        },
        'order.system': {
            'Meta': {'object_name': 'System'},
            'hotel_address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'hotel_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'order.table': {
            'Meta': {'object_name': 'Table'},
            'add_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'count': ('django.db.models.fields.IntegerField', [], {'default': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'personnum': ('django.db.models.fields.IntegerField', [], {'default': '4'}),
            'tablenum': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'tstatus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ttype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.Ttype']"})
        },
        'order.ttype': {
            'Meta': {'object_name': 'Ttype'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u'\\u5361\\u5ea7'", 'max_length': '50'})
        }
    }

    complete_apps = ['order']