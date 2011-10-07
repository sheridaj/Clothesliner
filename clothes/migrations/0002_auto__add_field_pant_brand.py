# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Pant.brand'
        db.add_column('clothes_pant', 'brand', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Pant.brand'
        db.delete_column('clothes_pant', 'brand')


    models = {
        'clothes.certification': {
            'Meta': {'object_name': 'Certification'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'clothes.closure': {
            'Meta': {'object_name': 'Closure'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'clothes.color': {
            'Meta': {'object_name': 'Color'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'clothes.designer': {
            'Meta': {'object_name': 'Designer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'webAddress': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'clothes.fabric': {
            'Meta': {'object_name': 'Fabric'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'clothes.fly': {
            'Meta': {'object_name': 'Fly'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'clothes.gender': {
            'Meta': {'object_name': 'Gender'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'clothes.origin': {
            'Meta': {'object_name': 'Origin'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'clothes.pant': {
            'Meta': {'object_name': 'Pant'},
            'back_rise': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'belt_loop_breadth': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'belt_loop_height': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'belt_loop_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'cargo_pocket_breadth': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cargo_pocket_depth': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cargo_pocket_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'certification': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clothes.Certification']", 'null': 'True', 'blank': 'True'}),
            'change_pocket_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'closure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clothes.Closure']", 'null': 'True', 'blank': 'True'}),
            'cuff': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cuff_unfinished': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'cut_on_bias': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'designer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clothes.Designer']", 'null': 'True', 'blank': 'True'}),
            'designer_inseam': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'designer_waist': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fabric': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clothes.Fabric']", 'null': 'True', 'blank': 'True'}),
            'fabric_dimensions': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fly': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clothes.Fly']", 'null': 'True', 'blank': 'True'}),
            'front_pocket_breadth': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'front_pocket_depth': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'front_pocket_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'front_pocket_style': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'front_style'", 'blank': 'True', 'null': 'True', 'to': "orm['clothes.Pocket_Style']"}),
            'front_rise': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clothes.Gender']", 'null': 'True', 'blank': 'True'}),
            'hidden_pocket_location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clothes.Pocket_Location']", 'null': 'True', 'blank': 'True'}),
            'hidden_pocket_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hips': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inseam': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'knee': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'manufacturing_location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'manufacture_location'", 'blank': 'True', 'null': 'True', 'to': "orm['clothes.Origin']"}),
            'material_origin': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'material_origin'", 'blank': 'True', 'null': 'True', 'to': "orm['clothes.Origin']"}),
            'organic': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'outseam': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pattern': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clothes.Pattern']", 'null': 'True', 'blank': 'True'}),
            'pattern_gap_size': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pattern_thickness': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pleat_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'preshrunk': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'primary_color': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'primary_color'", 'blank': 'True', 'null': 'True', 'to': "orm['clothes.Color']"}),
            'rear_pocket_breadth': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'rear_pocket_depth': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'rear_pocket_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rear_pocket_style': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rear_style'", 'blank': 'True', 'null': 'True', 'to': "orm['clothes.Pocket_Style']"}),
            'rivets': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'secondary_color': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'secondary_color'", 'blank': 'True', 'null': 'True', 'to': "orm['clothes.Color']"}),
            'style': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clothes.Style']", 'null': 'True', 'blank': 'True'}),
            'thigh': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'treatment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clothes.Treatment']", 'null': 'True', 'blank': 'True'}),
            'waist': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'waistband_curve': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'weave': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clothes.Weave']", 'null': 'True', 'blank': 'True'})
        },
        'clothes.pant_stock_item': {
            'Meta': {'object_name': 'Pant_Stock_Item'},
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dateAdded': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory_number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clothes.Pant']"}),
            'preferred': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'retailer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clothes.Retailer']"}),
            'url_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        },
        'clothes.pattern': {
            'Meta': {'object_name': 'Pattern'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'clothes.pocket_location': {
            'Meta': {'object_name': 'Pocket_Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'clothes.pocket_style': {
            'Meta': {'object_name': 'Pocket_Style'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'clothes.retailer': {
            'Meta': {'object_name': 'Retailer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'webAddress': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'clothes.style': {
            'Meta': {'object_name': 'Style'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'clothes.treatment': {
            'Meta': {'object_name': 'Treatment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'clothes.weave': {
            'Meta': {'object_name': 'Weave'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['clothes']
