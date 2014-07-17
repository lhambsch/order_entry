# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'DriveTimeCode.rate_currency'
        db.delete_column(u'estimates_drivetimecode', 'rate_currency')


        # Changing field 'DriveTimeCode.rate'
        db.alter_column(u'estimates_drivetimecode', 'rate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))
        # Deleting field 'Location.sales_tax_currency'
        db.delete_column(u'estimates_location', 'sales_tax_currency')


        # Changing field 'Location.sales_tax'
        db.alter_column(u'estimates_location', 'sales_tax', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2))
        # Deleting field 'Estimate.valuation_amount_currency'
        db.delete_column(u'estimates_estimate', 'valuation_amount_currency')

        # Deleting field 'Estimate.sales_tax_currency'
        db.delete_column(u'estimates_estimate', 'sales_tax_currency')


        # Changing field 'Estimate.valuation_amount'
        db.alter_column(u'estimates_estimate', 'valuation_amount', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Estimate.sales_tax'
        db.alter_column(u'estimates_estimate', 'sales_tax', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))
        # Deleting field 'Customer.balance_limit_amt_currency'
        db.delete_column(u'estimates_customer', 'balance_limit_amt_currency')

        # Deleting field 'Customer.job_limit_amt_currency'
        db.delete_column(u'estimates_customer', 'job_limit_amt_currency')


        # Changing field 'Customer.balance_limit_amt'
        db.alter_column(u'estimates_customer', 'balance_limit_amt', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

        # Changing field 'Customer.job_limit_amt'
        db.alter_column(u'estimates_customer', 'job_limit_amt', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))
        # Deleting field 'RateSchedule.location_id'
        db.delete_column(u'estimates_rateschedule', 'location_id_id')

        # Adding field 'RateSchedule.location'
        db.add_column(u'estimates_rateschedule', 'location',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='rate_schedules', null=True, blank=True, to=orm['estimates.Location']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'DriveTimeCode.rate_currency'
        db.add_column(u'estimates_drivetimecode', 'rate_currency',
                      self.gf('djmoney.models.fields.CurrencyField')(default='USD'),
                      keep_default=False)


        # Changing field 'DriveTimeCode.rate'
        db.alter_column(u'estimates_drivetimecode', 'rate', self.gf('djmoney.models.fields.MoneyField')(null=True, max_digits=10, decimal_places=2, default_currency='USD'))
        # Adding field 'Location.sales_tax_currency'
        db.add_column(u'estimates_location', 'sales_tax_currency',
                      self.gf('djmoney.models.fields.CurrencyField')(default='USD'),
                      keep_default=False)


        # Changing field 'Location.sales_tax'
        db.alter_column(u'estimates_location', 'sales_tax', self.gf('djmoney.models.fields.MoneyField')(max_digits=10, decimal_places=2, default_currency='USD'))
        # Adding field 'Estimate.valuation_amount_currency'
        db.add_column(u'estimates_estimate', 'valuation_amount_currency',
                      self.gf('djmoney.models.fields.CurrencyField')(),
                      keep_default=False)

        # Adding field 'Estimate.sales_tax_currency'
        db.add_column(u'estimates_estimate', 'sales_tax_currency',
                      self.gf('djmoney.models.fields.CurrencyField')(default='USD'),
                      keep_default=False)


        # Changing field 'Estimate.valuation_amount'
        db.alter_column(u'estimates_estimate', 'valuation_amount', self.gf('djmoney.models.fields.MoneyField')(null=True, max_digits=10, decimal_places=2, default_currency='XYZ'))

        # Changing field 'Estimate.sales_tax'
        db.alter_column(u'estimates_estimate', 'sales_tax', self.gf('djmoney.models.fields.MoneyField')(null=True, max_digits=10, decimal_places=2, default_currency='USD'))
        # Adding field 'Customer.balance_limit_amt_currency'
        db.add_column(u'estimates_customer', 'balance_limit_amt_currency',
                      self.gf('djmoney.models.fields.CurrencyField')(default='USD'),
                      keep_default=False)

        # Adding field 'Customer.job_limit_amt_currency'
        db.add_column(u'estimates_customer', 'job_limit_amt_currency',
                      self.gf('djmoney.models.fields.CurrencyField')(default='USD'),
                      keep_default=False)


        # Changing field 'Customer.balance_limit_amt'
        db.alter_column(u'estimates_customer', 'balance_limit_amt', self.gf('djmoney.models.fields.MoneyField')(null=True, max_digits=10, decimal_places=2, default_currency='USD'))

        # Changing field 'Customer.job_limit_amt'
        db.alter_column(u'estimates_customer', 'job_limit_amt', self.gf('djmoney.models.fields.MoneyField')(null=True, max_digits=10, decimal_places=2, default_currency='USD'))
        # Adding field 'RateSchedule.location_id'
        db.add_column(u'estimates_rateschedule', 'location_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='rate_schedules', to=orm['estimates.Location']),
                      keep_default=False)

        # Deleting field 'RateSchedule.location'
        db.delete_column(u'estimates_rateschedule', 'location_id')


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
            'effective_rate_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rate_schedules'", 'to': u"orm['estimates.EffectiveRate']"}),
            'expiration_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'rate_schedules'", 'null': 'True', 'blank': 'True', 'to': u"orm['estimates.Location']"}),
            'rate_schedule_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'requires_approval': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'estimates.status': {
            'Meta': {'object_name': 'Status'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {}),
            'status_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
        }
    }

    complete_apps = ['estimates']