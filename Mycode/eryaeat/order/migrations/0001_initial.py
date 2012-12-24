# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Recipe'
        db.create_table('order_recipe', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('rtype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['order.Rtype'])),
            ('discount', self.gf('django.db.models.fields.FloatField')(default=1.0)),
            ('rstatus', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('imgurl', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('comments', self.gf('django.db.models.fields.FloatField')(default=4)),
            ('shelfdate', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('order', ['Recipe'])

        # Adding model 'Rtype'
        db.create_table('order_rtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('sequence', self.gf('django.db.models.fields.IntegerField')(default=9)),
        ))
        db.send_create_signal('order', ['Rtype'])

        # Adding model 'Table'
        db.create_table('order_table', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tablenum', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('personnum', self.gf('django.db.models.fields.IntegerField')(default=4)),
            ('tstatus', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ttype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['order.Ttype'])),
            ('count', self.gf('django.db.models.fields.IntegerField')(default=50)),
            ('add_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('order', ['Table'])

        # Adding model 'Ttype'
        db.create_table('order_ttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default=u'\u5361\u5ea7', max_length=50)),
        ))
        db.send_create_signal('order', ['Ttype'])

        # Adding model 'Order'
        db.create_table('order_order', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tablenum', self.gf('django.db.models.fields.IntegerField')()),
            ('personnum', self.gf('django.db.models.fields.IntegerField')()),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('order', ['Order'])

        # Adding M2M table for field recipe on 'Order'
        db.create_table('order_order_recipe', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('order', models.ForeignKey(orm['order.order'], null=False)),
            ('recipe', models.ForeignKey(orm['order.recipe'], null=False))
        ))
        db.create_unique('order_order_recipe', ['order_id', 'recipe_id'])

        # Adding model 'Depot'
        db.create_table('order_depot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('orderno', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('table', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['order.Table'])),
            ('add_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('order', ['Depot'])

        # Adding model 'Detail'
        db.create_table('order_detail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('depot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['order.Depot'])),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['order.Recipe'])),
            ('add_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('order', ['Detail'])

        # Adding model 'Phoneid'
        db.create_table('order_phoneid', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('table', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['order.Table'])),
        ))
        db.send_create_signal('order', ['Phoneid'])

        # Adding model 'System'
        db.create_table('order_system', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hotel_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('hotel_address', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('order', ['System'])


    def backwards(self, orm):
        # Deleting model 'Recipe'
        db.delete_table('order_recipe')

        # Deleting model 'Rtype'
        db.delete_table('order_rtype')

        # Deleting model 'Table'
        db.delete_table('order_table')

        # Deleting model 'Ttype'
        db.delete_table('order_ttype')

        # Deleting model 'Order'
        db.delete_table('order_order')

        # Removing M2M table for field recipe on 'Order'
        db.delete_table('order_order_recipe')

        # Deleting model 'Depot'
        db.delete_table('order_depot')

        # Deleting model 'Detail'
        db.delete_table('order_detail')

        # Deleting model 'Phoneid'
        db.delete_table('order_phoneid')

        # Deleting model 'System'
        db.delete_table('order_system')


    models = {
        'order.depot': {
            'Meta': {'object_name': 'Depot'},
            'add_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'orderno': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'table': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['order.Table']"})
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'personnum': ('django.db.models.fields.IntegerField', [], {}),
            'recipe': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['order.Recipe']", 'symmetrical': 'False'}),
            'tablenum': ('django.db.models.fields.IntegerField', [], {})
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