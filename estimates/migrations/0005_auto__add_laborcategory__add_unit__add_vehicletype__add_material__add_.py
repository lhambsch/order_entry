# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LaborCategory'
        db.create_table(u'estimates_laborcategory', (
            ('labor_category_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'estimates', ['LaborCategory'])

        # Adding model 'Unit'
        db.create_table(u'estimates_unit', (
            ('unit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('unit_of_measure', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('unit_type', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('minutes_per_unit', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.CharField')(default='admin', max_length=50)),
        ))
        db.send_create_signal(u'estimates', ['Unit'])

        # Adding model 'VehicleType'
        db.create_table(u'estimates_vehicletype', (
            ('vehicle_type_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('is_inventory_item', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_default', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'estimates', ['VehicleType'])

        # Adding model 'Material'
        db.create_table(u'estimates_material', (
            ('material_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('is_default', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('minutes_to_pack', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.CharField')(default='admin', max_length=50)),
        ))
        db.send_create_signal(u'estimates', ['Material'])

        # Adding model 'WorkOrderEquipmentItem'
        db.create_table(u'estimates_workorderequipmentitem', (
            ('work_order_equipment_item_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('work_order', self.gf('django.db.models.fields.related.ForeignKey')(related_name='work_order_equipment_items', to=orm['estimates.WorkOrder'])),
            ('equipment_item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='work_order_equipment_items', to=orm['estimates.EquipmentItem'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.CharField')(default='admin', max_length=50)),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.CharField')(default='admin', max_length=50)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'estimates', ['WorkOrderEquipmentItem'])

        # Adding model 'WorkOrderInstallService'
        db.create_table(u'estimates_workorderinstallservice', (
            ('work_order_install_service_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('work_order', self.gf('django.db.models.fields.related.ForeignKey')(related_name='work_order_install_services', to=orm['estimates.WorkOrder'])),
            ('installation_service', self.gf('django.db.models.fields.related.ForeignKey')(related_name='work_order_install_services', to=orm['estimates.InstallationService'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('shifts', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('men', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('man_hours', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('travel_time', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('crew_hours', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('rt_hours', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('ot_hours', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('pt_hours', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.CharField')(default='admin', max_length=50)),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.CharField')(default='admin', max_length=50)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'estimates', ['WorkOrderInstallService'])

        # Adding model 'WorkOrderUnit'
        db.create_table(u'estimates_workorderunit', (
            ('work_order_unit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('work_order', self.gf('django.db.models.fields.related.ForeignKey')(related_name='work_order_units', to=orm['estimates.WorkOrder'])),
            ('unit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='work_order_units', to=orm['estimates.Unit'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('cost', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.CharField')(default='admin', max_length=50)),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.CharField')(default='admin', max_length=50)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'estimates', ['WorkOrderUnit'])

        # Adding model 'WorkOrderComment'
        db.create_table(u'estimates_workordercomment', (
            ('work_order_comment_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('work_order', self.gf('django.db.models.fields.related.ForeignKey')(related_name='work_order_comments', to=orm['estimates.WorkOrder'])),
            ('comment', self.gf('django.db.models.fields.TextField')(default='')),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.CharField')(default='admin', max_length=50)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'estimates', ['WorkOrderComment'])

        # Adding model 'InstallationService'
        db.create_table(u'estimates_installationservice', (
            ('installation_service_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('minutes_to_install', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.CharField')(default='admin', max_length=50)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'estimates', ['InstallationService'])

        # Adding model 'WorkOrderMaterial'
        db.create_table(u'estimates_workordermaterial', (
            ('work_order_material_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('work_order', self.gf('django.db.models.fields.related.ForeignKey')(related_name='work_order_materials', to=orm['estimates.WorkOrder'])),
            ('material', self.gf('django.db.models.fields.related.ForeignKey')(related_name='work_order_materials', to=orm['estimates.Material'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('cost', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.CharField')(default='admin', max_length=50)),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.CharField')(default='admin', max_length=50)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'estimates', ['WorkOrderMaterial'])

        # Adding model 'WorkOrderLaborTask'
        db.create_table(u'estimates_workorderlabortask', (
            ('work_order_labor_task_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('work_order', self.gf('django.db.models.fields.related.ForeignKey')(related_name='work_order_labor_tasks', to=orm['estimates.WorkOrder'])),
            ('labor_task', self.gf('django.db.models.fields.related.ForeignKey')(related_name='work_order_labor_tasks', to=orm['estimates.LaborTask'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total_hours', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('reg_hours', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('reg_rate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('ot_hours', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('ot_rate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('pt_hours', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('pt_rate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('total_cost', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.CharField')(default='admin', max_length=50)),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.CharField')(default='admin', max_length=50)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'estimates', ['WorkOrderLaborTask'])

        # Adding model 'LaborTask'
        db.create_table(u'estimates_labortask', (
            ('labor_task_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('labor_category', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='labor_tasks', null=True, to=orm['estimates.LaborCategory'])),
        ))
        db.send_create_signal(u'estimates', ['LaborTask'])

        # Adding model 'WorkOrderVehicle'
        db.create_table(u'estimates_workordervehicle', (
            ('work_order_vehicle_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('work_order', self.gf('django.db.models.fields.related.ForeignKey')(related_name='work_order_vehicles', to=orm['estimates.WorkOrder'])),
            ('vehicle_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='work_order_vehicles', to=orm['estimates.VehicleType'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.CharField')(default='admin', max_length=50)),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.CharField')(default='admin', max_length=50)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'estimates', ['WorkOrderVehicle'])

        # Adding model 'EquipmentItem'
        db.create_table(u'estimates_equipmentitem', (
            ('equipment_item_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('is_inventory_item', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_default', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'estimates', ['EquipmentItem'])


    def backwards(self, orm):
        # Deleting model 'LaborCategory'
        db.delete_table(u'estimates_laborcategory')

        # Deleting model 'Unit'
        db.delete_table(u'estimates_unit')

        # Deleting model 'VehicleType'
        db.delete_table(u'estimates_vehicletype')

        # Deleting model 'Material'
        db.delete_table(u'estimates_material')

        # Deleting model 'WorkOrderEquipmentItem'
        db.delete_table(u'estimates_workorderequipmentitem')

        # Deleting model 'WorkOrderInstallService'
        db.delete_table(u'estimates_workorderinstallservice')

        # Deleting model 'WorkOrderUnit'
        db.delete_table(u'estimates_workorderunit')

        # Deleting model 'WorkOrderComment'
        db.delete_table(u'estimates_workordercomment')

        # Deleting model 'InstallationService'
        db.delete_table(u'estimates_installationservice')

        # Deleting model 'WorkOrderMaterial'
        db.delete_table(u'estimates_workordermaterial')

        # Deleting model 'WorkOrderLaborTask'
        db.delete_table(u'estimates_workorderlabortask')

        # Deleting model 'LaborTask'
        db.delete_table(u'estimates_labortask')

        # Deleting model 'WorkOrderVehicle'
        db.delete_table(u'estimates_workordervehicle')

        # Deleting model 'EquipmentItem'
        db.delete_table(u'estimates_equipmentitem')


    models = {
        u'estimates.additionalchargetype': {
            'Meta': {'object_name': 'AdditionalChargeType'},
            'additional_charge_type_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'approval': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'estimates.competitor': {
            'Meta': {'object_name': 'Competitor'},
            'competitor_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'estimates.contact': {
            'Meta': {'object_name': 'Contact'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'appointment_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'business_phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'contact_title': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contacts'", 'null': 'True', 'to': u"orm['estimates.ContactTitle']"}),
            'contact_title_other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts'", 'to': u"orm['estimates.Customer']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'hot_list': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_primary_contact': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'linkedin_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'next_call_back': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'next_step': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'other_phone_1': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'other_phone_2': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'other_phone_3': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'phone_ext': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'phone_ext_1': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'phone_ext_2': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contacts'", 'null': 'True', 'to': u"orm['estimates.Status']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'website_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'estimates.contacttitle': {
            'Meta': {'object_name': 'ContactTitle'},
            'contact_title_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'estimates.contractor': {
            'Meta': {'object_name': 'Contractor'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'contractor_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'end_pay_period': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'is_payroll': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contractors'", 'to': u"orm['estimates.Location']"}),
            'modified_by': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'pr_location_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'start_pay_period': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contractors'", 'to': u"orm['estimates.Status']"}),
            'track_lead': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'vendor_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'estimates.customer': {
            'Meta': {'object_name': 'Customer'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'balance_limit_amt': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'bill_address_1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'bill_address_2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'bill_attn_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'bill_city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'bill_customer_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'bill_email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'bill_fax': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'bill_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'bill_phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'bill_phone_ext': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'bill_state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'bill_zip': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'consumable_charge_percentage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'customer_code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'customer_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'customer_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'customer_no': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'customer_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'customers'", 'null': 'True', 'to': u"orm['estimates.CustomerType']"}),
            'drive_time_code': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'customers'", 'null': 'True', 'to': u"orm['estimates.DriveTimeCode']"}),
            'employee_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'energy_charge_percentage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'exempt_consumable_supply': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'exempt_energy_charge': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'exempt_equipment_load_time': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'exempt_sales_tax': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'furniture_competitor': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'furniture_customers'", 'null': 'True', 'to': u"orm['estimates.Competitor']"}),
            'furniture_competitor_other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'great_plains_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'hot_list': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'installation_competitor': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'installation_customers'", 'null': 'True', 'to': u"orm['estimates.Competitor']"}),
            'installation_competitor_other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'is_cov_u': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_prevailing_wage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_prospect': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_roi_prospect': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_web_order': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'job_limit_amt': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'last_credit_check': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'customers'", 'null': 'True', 'to': u"orm['estimates.Location']"}),
            'logistics_competitor': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'logistics_customers'", 'null': 'True', 'to': u"orm['estimates.Competitor']"}),
            'logistics_competitor_other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'moving_competitor': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'moving_customers'", 'null': 'True', 'to': u"orm['estimates.Competitor']"}),
            'moving_competitor_other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'overtime_code': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'customers'", 'null': 'True', 'to': u"orm['estimates.OvertimeCode']"}),
            'overtime_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'customers'", 'null': 'True', 'to': u"orm['estimates.OvertimeType']"}),
            'parent_customer': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['estimates.Customer']"}),
            'payment_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'customers'", 'null': 'True', 'to': u"orm['estimates.PaymentType']"}),
            'rate_schedule': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'customers'", 'null': 'True', 'to': u"orm['estimates.RateSchedule']"}),
            'show_consumable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_energy_charge': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'customers'", 'null': 'True', 'to': u"orm['estimates.Status']"}),
            'tech_competitor': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tech_customers'", 'null': 'True', 'to': u"orm['estimates.Competitor']"}),
            'tech_competitor_other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'terms_and_conditions': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'valuation_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'customers'", 'null': 'True', 'to': u"orm['estimates.ValuationType']"}),
            'warehouse_competitor': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'warehouse_customers'", 'null': 'True', 'to': u"orm['estimates.Competitor']"}),
            'warehouse_competitor_other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'website_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'estimates.customeraddress': {
            'Meta': {'object_name': 'CustomerAddress'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '31', 'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'customer_addresses'", 'null': 'True', 'to': u"orm['estimates.Customer']"}),
            'customer_address_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '29', 'null': 'True', 'blank': 'True'}),
            'street_1': ('django.db.models.fields.CharField', [], {'max_length': '31', 'null': 'True', 'blank': 'True'}),
            'street_2': ('django.db.models.fields.CharField', [], {'max_length': '31', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '14', 'null': 'True', 'blank': 'True'})
        },
        u'estimates.customertype': {
            'Meta': {'object_name': 'CustomerType'},
            'customer_type_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'estimates.drivetimecode': {
            'Meta': {'object_name': 'DriveTimeCode'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'drive_time_code_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'estimates.effectiverate': {
            'Meta': {'object_name': 'EffectiveRate'},
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'effective_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'effective_rate_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'expiration_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'estimates.equipmentitem': {
            'Meta': {'object_name': 'EquipmentItem'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'equipment_item_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_inventory_item': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'estimates.estimate': {
            'Meta': {'object_name': 'Estimate'},
            'approved_by': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'approved_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'bc_loads': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'booking_branch': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'estimates'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['estimates.Location']"}),
            'cartons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'confirmed_by': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'confirmed_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'consumable_charge_is_optional': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'consumable_charge_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'consumable_estimates'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['estimates.AdditionalChargeType']"}),
            'consumable_pct': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'estimates'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['estimates.Contact']"}),
            'contract_no': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'contractor': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'estimates'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['estimates.Contractor']"}),
            'converted_by': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'converted_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'crates': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'estimates'", 'to': u"orm['estimates.Customer']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'dolly_loads': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'drive_time_code': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'estimates'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['estimates.DriveTimeCode']"}),
            'energy_charge_is_optional': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'energy_charge_pct': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'energy_charge_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'energy_estimates'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['estimates.AdditionalChargeType']"}),
            'estimate_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'estimate_no': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'estimate_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'estimates'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['estimates.EstimateType']"}),
            'head_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'instructions': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'is_prevailing_wage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'job_rcvd_by': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'job_rcvd_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'job_rcvd_from': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'mc_loads': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'other_loads': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'overtime_code': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'estimates'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['estimates.OvertimeCode']"}),
            'overtime_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'estimates'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['estimates.OvertimeType']"}),
            'pc_loads': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'po_no': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'prevailing_wage': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'estimates'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['estimates.PrevailingWage']"}),
            'pricing_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'estimates'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['estimates.PricingType']"}),
            'proposal_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'estimates'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['estimates.ProposalType']"}),
            'rate_schedule': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'estimates'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['estimates.RateSchedule']"}),
            'sales_tax': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'sales_tax_pct': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'security_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'square_feet': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'estimates'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['estimates.Status']"}),
            'submitted_by': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'submitted_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'tub_loads': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'valuation_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'valuation_is_optional': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'valuation_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'estimates'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['estimates.ValuationType']"})
        },
        u'estimates.estimatetype': {
            'Meta': {'object_name': 'EstimateType'},
            'estimate_type_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'estimates.installationservice': {
            'Meta': {'object_name': 'InstallationService'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created_by': ('django.db.models.fields.CharField', [], {'default': "'admin'", 'max_length': '50'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'installation_service_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minutes_to_install': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'estimates.laborcategory': {
            'Meta': {'object_name': 'LaborCategory'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'labor_category_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'estimates.labortask': {
            'Meta': {'object_name': 'LaborTask'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'labor_category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'labor_tasks'", 'null': 'True', 'to': u"orm['estimates.LaborCategory']"}),
            'labor_task_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'task': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'estimates.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_service_branch': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_terminal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'job_no_prefix': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'location_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'sales_tax': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'estimates.material': {
            'Meta': {'object_name': 'Material'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created_by': ('django.db.models.fields.CharField', [], {'default': "'admin'", 'max_length': '50'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'material_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minutes_to_pack': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'estimates.overtimecode': {
            'Meta': {'object_name': 'OvertimeCode'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'overtime': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'overtime_code_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'overtime_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'overtime_codes'", 'to': u"orm['estimates.OvertimeType']"}),
            'premium_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'time_in': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'time_out': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'estimates.overtimetype': {
            'Meta': {'object_name': 'OvertimeType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'overtime_type_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'estimates.paymenttype': {
            'Meta': {'object_name': 'PaymentType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'payment_type_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'estimates.prevailingwage': {
            'Meta': {'object_name': 'PrevailingWage'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'prevailing_wage_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'estimates.pricingtype': {
            'Meta': {'object_name': 'PricingType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pricing_type_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'estimates.proposaltype': {
            'Meta': {'object_name': 'ProposalType'},
            'proposal_type_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'estimates.rateschedule': {
            'Meta': {'object_name': 'RateSchedule'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'effective_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'effective_rate': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'rate_schedules'", 'null': 'True', 'blank': 'True', 'to': u"orm['estimates.EffectiveRate']"}),
            'expiration_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'rate_schedules'", 'null': 'True', 'blank': 'True', 'to': u"orm['estimates.Location']"}),
            'rate_schedule_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'requires_approval': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'estimates.serviceline': {
            'Meta': {'object_name': 'ServiceLine'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'energy_surcharge': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_billing': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_roi': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_tl_supported': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'service': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'service_line_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'estimates.status': {
            'Meta': {'object_name': 'Status'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {}),
            'status_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'estimates.unit': {
            'Meta': {'object_name': 'Unit'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created_by': ('django.db.models.fields.CharField', [], {'default': "'admin'", 'max_length': '50'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'minutes_per_unit': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'unit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'unit_of_measure': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'unit_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'estimates.valuationtype': {
            'Meta': {'object_name': 'ValuationType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'factor': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'is_flat_fee': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rpt_description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {}),
            'valuation_type_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'estimates.vehicletype': {
            'Meta': {'object_name': 'VehicleType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_inventory_item': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'vehicle_type_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'estimates.workorder': {
            'Meta': {'object_name': 'WorkOrder'},
            'clone_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'clone_from': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'depart_military_time': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'depart_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'destination_contact': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'destination_contact_work_orders'", 'null': 'True', 'to': u"orm['estimates.Contact']"}),
            'destination_location': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'destination_work_orders'", 'null': 'True', 'to': u"orm['estimates.CustomerAddress']"}),
            'estimate': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'work_orders'", 'null': 'True', 'to': u"orm['estimates.Estimate']"}),
            'estimated_hours': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'general_relocation_cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'installation_cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'installation_hardware_cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'instructions': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'labor_cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'material_cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'on_site_military_time': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'on_site_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'origin_contact': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'origin_contact_work_orders'", 'null': 'True', 'to': u"orm['estimates.Contact']"}),
            'origin_location': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'origin_work_orders'", 'null': 'True', 'to': u"orm['estimates.CustomerAddress']"}),
            'original_group': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'original_group_work_orders'", 'null': 'True', 'to': u"orm['estimates.WorkOrderGroup']"}),
            'packing_cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'packing_material_cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'service_branch': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'work_orders'", 'null': 'True', 'to': u"orm['estimates.Location']"}),
            'service_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'service_line': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'work_orders'", 'null': 'True', 'to': u"orm['estimates.ServiceLine']"}),
            'services_total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'work_orders'", 'null': 'True', 'to': u"orm['estimates.Status']"}),
            'storage_cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'tech_supply_cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'tech_work_cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'unitized_cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'work_order_group': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'current_group_work_orders'", 'null': 'True', 'to': u"orm['estimates.WorkOrderGroup']"}),
            'work_order_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'work_order_no': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'estimates.workordercomment': {
            'Meta': {'object_name': 'WorkOrderComment'},
            'comment': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'created_by': ('django.db.models.fields.CharField', [], {'default': "'admin'", 'max_length': '50'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'work_order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'work_order_comments'", 'to': u"orm['estimates.WorkOrder']"}),
            'work_order_comment_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'estimates.workorderequipmentitem': {
            'Meta': {'object_name': 'WorkOrderEquipmentItem'},
            'created_by': ('django.db.models.fields.CharField', [], {'default': "'admin'", 'max_length': '50'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'equipment_item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'work_order_equipment_items'", 'to': u"orm['estimates.EquipmentItem']"}),
            'modified_by': ('django.db.models.fields.CharField', [], {'default': "'admin'", 'max_length': '50'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'work_order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'work_order_equipment_items'", 'to': u"orm['estimates.WorkOrder']"}),
            'work_order_equipment_item_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'estimates.workordergroup': {
            'Meta': {'object_name': 'WorkOrderGroup'},
            'add_to_total': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'estimate': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'work_order_groups'", 'null': 'True', 'to': u"orm['estimates.Estimate']"}),
            'group_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'group_total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'work_order_group_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'estimates.workorderinstallservice': {
            'Meta': {'object_name': 'WorkOrderInstallService'},
            'created_by': ('django.db.models.fields.CharField', [], {'default': "'admin'", 'max_length': '50'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'crew_hours': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'installation_service': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'work_order_install_services'", 'to': u"orm['estimates.InstallationService']"}),
            'man_hours': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'men': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'modified_by': ('django.db.models.fields.CharField', [], {'default': "'admin'", 'max_length': '50'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'ot_hours': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'pt_hours': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rt_hours': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'shifts': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'travel_time': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'work_order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'work_order_install_services'", 'to': u"orm['estimates.WorkOrder']"}),
            'work_order_install_service_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'estimates.workorderlabortask': {
            'Meta': {'object_name': 'WorkOrderLaborTask'},
            'created_by': ('django.db.models.fields.CharField', [], {'default': "'admin'", 'max_length': '50'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'labor_task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'work_order_labor_tasks'", 'to': u"orm['estimates.LaborTask']"}),
            'modified_by': ('django.db.models.fields.CharField', [], {'default': "'admin'", 'max_length': '50'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'ot_hours': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'ot_rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'pt_hours': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'pt_rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'reg_hours': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'reg_rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'total_hours': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'work_order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'work_order_labor_tasks'", 'to': u"orm['estimates.WorkOrder']"}),
            'work_order_labor_task_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'estimates.workordermaterial': {
            'Meta': {'object_name': 'WorkOrderMaterial'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'default': "'admin'", 'max_length': '50'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'work_order_materials'", 'to': u"orm['estimates.Material']"}),
            'modified_by': ('django.db.models.fields.CharField', [], {'default': "'admin'", 'max_length': '50'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'work_order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'work_order_materials'", 'to': u"orm['estimates.WorkOrder']"}),
            'work_order_material_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'estimates.workorderunit': {
            'Meta': {'object_name': 'WorkOrderUnit'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'default': "'admin'", 'max_length': '50'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.CharField', [], {'default': "'admin'", 'max_length': '50'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'work_order_units'", 'to': u"orm['estimates.Unit']"}),
            'work_order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'work_order_units'", 'to': u"orm['estimates.WorkOrder']"}),
            'work_order_unit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'estimates.workordervehicle': {
            'Meta': {'object_name': 'WorkOrderVehicle'},
            'created_by': ('django.db.models.fields.CharField', [], {'default': "'admin'", 'max_length': '50'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.CharField', [], {'default': "'admin'", 'max_length': '50'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'vehicle_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'work_order_vehicles'", 'to': u"orm['estimates.VehicleType']"}),
            'work_order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'work_order_vehicles'", 'to': u"orm['estimates.WorkOrder']"}),
            'work_order_vehicle_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['estimates']