# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Order.billing_address'
        db.add_column('shop_order', 'billing_address', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='the_billing_address', null=True, to=orm['trikotonshop.Address']), keep_default=False)

        # Adding field 'Order.shipping_address'
        db.add_column('shop_order', 'shipping_address', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='the_shipping_address', null=True, to=orm['trikotonshop.Address']), keep_default=False)

        # Adding field 'CartItem.size'
        db.add_column('shop_cartitem', 'size', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trikotonshop.Sizes'], null=True, blank=True), keep_default=False)

        # Adding field 'CartItem.audio_id'
        db.add_column('shop_cartitem', 'audio_id', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding M2M table for field knitting_color on 'CartItem'
        db.create_table('shop_cartitem_knitting_color', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cartitem', models.ForeignKey(orm['shop.cartitem'], null=False)),
            ('knittingcolor', models.ForeignKey(orm['trikotonshop.knittingcolor'], null=False))
        ))
        db.create_unique('shop_cartitem_knitting_color', ['cartitem_id', 'knittingcolor_id'])

        # Adding field 'OrderItem.size'
        db.add_column('shop_orderitem', 'size', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trikotonshop.Sizes'], null=True, blank=True), keep_default=False)

        # Adding field 'OrderItem.audio_id'
        db.add_column('shop_orderitem', 'audio_id', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'OrderItem.jacquar_file'
        db.add_column('shop_orderitem', 'jacquar_file', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'OrderItem.trikoton_code'
        db.add_column('shop_orderitem', 'trikoton_code', self.gf('django.db.models.fields.CharField')(max_length=6, null=True, blank=True), keep_default=False)

        # Adding M2M table for field knitting_color on 'OrderItem'
        db.create_table('shop_orderitem_knitting_color', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('orderitem', models.ForeignKey(orm['shop.orderitem'], null=False)),
            ('knittingcolor', models.ForeignKey(orm['trikotonshop.knittingcolor'], null=False))
        ))
        db.create_unique('shop_orderitem_knitting_color', ['orderitem_id', 'knittingcolor_id'])


    def backwards(self, orm):
        
        # Deleting field 'Order.billing_address'
        db.delete_column('shop_order', 'billing_address_id')

        # Deleting field 'Order.shipping_address'
        db.delete_column('shop_order', 'shipping_address_id')

        # Deleting field 'CartItem.size'
        db.delete_column('shop_cartitem', 'size_id')

        # Deleting field 'CartItem.audio_id'
        db.delete_column('shop_cartitem', 'audio_id')

        # Removing M2M table for field knitting_color on 'CartItem'
        db.delete_table('shop_cartitem_knitting_color')

        # Deleting field 'OrderItem.size'
        db.delete_column('shop_orderitem', 'size_id')

        # Deleting field 'OrderItem.audio_id'
        db.delete_column('shop_orderitem', 'audio_id')

        # Deleting field 'OrderItem.jacquar_file'
        db.delete_column('shop_orderitem', 'jacquar_file')

        # Deleting field 'OrderItem.trikoton_code'
        db.delete_column('shop_orderitem', 'trikoton_code')

        # Removing M2M table for field knitting_color on 'OrderItem'
        db.delete_table('shop_orderitem_knitting_color')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'shop.cart': {
            'Meta': {'object_name': 'Cart'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        'shop.cartitem': {
            'Meta': {'object_name': 'CartItem'},
            'audio_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': "orm['shop.Cart']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'knitting_color': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['trikotonshop.KnittingColor']", 'symmetrical': 'False'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'size': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['trikotonshop.Sizes']", 'null': 'True', 'blank': 'True'})
        },
        'shop.extraorderitempricefield': {
            'Meta': {'object_name': 'ExtraOrderItemPriceField'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.OrderItem']"}),
            'value': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '12', 'decimal_places': '2'})
        },
        'shop.extraorderpricefield': {
            'Meta': {'object_name': 'ExtraOrderPriceField'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_shipping': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Order']"}),
            'value': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '12', 'decimal_places': '2'})
        },
        'shop.order': {
            'Meta': {'object_name': 'Order'},
            'billing_address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'the_billing_address'", 'null': 'True', 'to': "orm['trikotonshop.Address']"}),
            'billing_address_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'order_subtotal': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '12', 'decimal_places': '2'}),
            'order_total': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '12', 'decimal_places': '2'}),
            'shipping_address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'the_shipping_address'", 'null': 'True', 'to': "orm['trikotonshop.Address']"}),
            'shipping_address_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'shop.orderextrainfo': {
            'Meta': {'object_name': 'OrderExtraInfo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'extra_info'", 'to': "orm['shop.Order']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'shop.orderitem': {
            'Meta': {'object_name': 'OrderItem'},
            'audio_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jacquar_file': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'knitting_color': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['trikotonshop.KnittingColor']", 'symmetrical': 'False'}),
            'line_subtotal': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '12', 'decimal_places': '2'}),
            'line_total': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '12', 'decimal_places': '2'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': "orm['shop.Order']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Product']", 'null': 'True', 'blank': 'True'}),
            'product_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'product_reference': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'size': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['trikotonshop.Sizes']", 'null': 'True', 'blank': 'True'}),
            'trikoton_code': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '12', 'decimal_places': '2'})
        },
        'shop.orderpayment': {
            'Meta': {'object_name': 'OrderPayment'},
            'amount': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '12', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Order']"}),
            'payment_method': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'transaction_id': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'shop.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_shop.product_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '12', 'decimal_places': '2'})
        },
        'trikotonshop.address': {
            'Meta': {'object_name': 'Address'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['trikotonshop.Country']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_billing': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'billing_address'", 'unique': 'True', 'null': 'True', 'to': "orm['auth.User']"}),
            'user_shipping': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'shipping_address'", 'unique': 'True', 'null': 'True', 'to': "orm['auth.User']"}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'trikotonshop.country': {
            'Meta': {'object_name': 'Country'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'shipping_zone': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '10'})
        },
        'trikotonshop.knittingcolor': {
            'Meta': {'object_name': 'KnittingColor'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'color_display_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'production_code': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'trikotonshop.sizes': {
            'Meta': {'object_name': 'Sizes'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['shop']
