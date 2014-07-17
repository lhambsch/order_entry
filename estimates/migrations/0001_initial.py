# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Status'
        db.create_table(u'estimates_status', (
            ('status_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'estimates', ['Status'])

        # Adding model 'CustomerType'
        db.create_table(u'estimates_customertype', (
            ('customer_type_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'estimates', ['CustomerType'])

        # Adding model 'OvertimeType'
        db.create_table(u'estimates_overtimetype', (
            ('overtime_type_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'estimates', ['OvertimeType'])

        # Adding model 'DriveTimeCode'
        db.create_table(u'estimates_drivetimecode', (
            ('drive_time_code_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')()),
            ('rate_currency', self.gf('djmoney.models.fields.CurrencyField')(default='USD')),
            ('rate', self.gf('djmoney.models.fields.MoneyField')(default_currency='USD', null=True, max_digits=10, decimal_places=2, blank=True)),
        ))
        db.send_create_signal(u'estimates', ['DriveTimeCode'])

        # Adding model 'ValuationType'
        db.create_table(u'estimates_valuationtype', (
            ('valuation_type_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rpt_description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('is_flat_fee', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('factor', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'estimates', ['ValuationType'])

        # Adding model 'PaymentType'
        db.create_table(u'estimates_paymenttype', (
            ('payment_type_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'estimates', ['PaymentType'])

        # Adding model 'Competitor'
        db.create_table(u'estimates_competitor', (
            ('competitor_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('created_by', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'estimates', ['Competitor'])

        # Adding model 'OvertimeCode'
        db.create_table(u'estimates_overtimecode', (
            ('overtime_code_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('overtime_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='overtime_codes', to=orm['estimates.OvertimeType'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('overtime', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('premium_time', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('time_in', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('time_out', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'estimates', ['OvertimeCode'])

        # Adding model 'Location'
        db.create_table(u'estimates_location', (
            ('location_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('job_no_prefix', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sales_tax_currency', self.gf('djmoney.models.fields.CurrencyField')(default='USD')),
            ('sales_tax', self.gf('djmoney.models.fields.MoneyField')(max_digits=10, decimal_places=2, default_currency='USD')),
            ('is_terminal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_service_branch', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'estimates', ['Location'])

        # Adding model 'EffectiveRate'
        db.create_table(u'estimates_effectiverate', (
            ('effective_rate_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('effective_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('expiration_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'estimates', ['EffectiveRate'])

        # Adding model 'RateSchedule'
        db.create_table(u'estimates_rateschedule', (
            ('rate_schedule_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rate_schedules', to=orm['estimates.Location'])),
            ('effective_rate_id', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rate_schedules', to=orm['estimates.EffectiveRate'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('effective_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('expiration_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')()),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('requires_approval', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'estimates', ['RateSchedule'])

        # Adding model 'Customer'
        db.create_table(u'estimates_customer', (
            ('customer_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent_customer', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['estimates.Customer'])),
            ('customer_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='customers', null=True, to=orm['estimates.CustomerType'])),
            ('overtime_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='customers', null=True, to=orm['estimates.OvertimeType'])),
            ('drive_time_code', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='customers', null=True, to=orm['estimates.DriveTimeCode'])),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='customers', null=True, to=orm['estimates.Status'])),
            ('valuation_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='customers', null=True, to=orm['estimates.ValuationType'])),
            ('payment_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='customers', null=True, to=orm['estimates.PaymentType'])),
            ('customer_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('customer_code', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('customer_no', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('exempt_sales_tax', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('exempt_equipment_load_time', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_prevailing_wage', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('exempt_energy_charge', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('exempt_consumable_supply', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('address_1', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('address_2', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('balance_limit_amt_currency', self.gf('djmoney.models.fields.CurrencyField')(default='USD')),
            ('balance_limit_amt', self.gf('djmoney.models.fields.MoneyField')(default_currency='USD', null=True, max_digits=10, decimal_places=2, blank=True)),
            ('job_limit_amt_currency', self.gf('djmoney.models.fields.CurrencyField')(default='USD')),
            ('job_limit_amt', self.gf('djmoney.models.fields.MoneyField')(default_currency='USD', null=True, max_digits=10, decimal_places=2, blank=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('energy_charge_percentage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('consumable_charge_percentage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('great_plains_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('last_credit_check', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('terms_and_conditions', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('website_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('furniture_competitor', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='furniture_customers', null=True, to=orm['estimates.Competitor'])),
            ('furniture_competitor_other', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('installation_competitor', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='installation_customers', null=True, to=orm['estimates.Competitor'])),
            ('installation_competitor_other', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('warehouse_competitor', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='warehouse_customers', null=True, to=orm['estimates.Competitor'])),
            ('warehouse_competitor_other', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('tech_competitor', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='tech_customers', null=True, to=orm['estimates.Competitor'])),
            ('tech_competitor_other', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('logistics_competitor', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='logistics_customers', null=True, to=orm['estimates.Competitor'])),
            ('logistics_competitor_other', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('moving_competitor', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='moving_customers', null=True, to=orm['estimates.Competitor'])),
            ('moving_competitor_other', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('is_prospect', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('overtime_code', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='customers', null=True, to=orm['estimates.OvertimeCode'])),
            ('hot_list', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_roi_prospect', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('bill_customer_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('bill_attn_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('bill_address_1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('bill_address_2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('bill_city', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('bill_state', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('bill_zip', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('bill_phone', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('bill_phone_ext', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('bill_fax', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('bill_email', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('bill_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('rate_schedule', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='customers', null=True, to=orm['estimates.RateSchedule'])),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='customers', null=True, to=orm['estimates.Location'])),
            ('is_web_order', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_cov_u', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('show_consumable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('show_energy_charge', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('employee_count', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'estimates', ['Customer'])

        # Adding model 'ContactTitle'
        db.create_table(u'estimates_contacttitle', (
            ('contact_title_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created_by', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'estimates', ['ContactTitle'])

        # Adding model 'Contact'
        db.create_table(u'estimates_contact', (
            ('contact_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contacts', to=orm['estimates.Customer'])),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='contacts', null=True, to=orm['estimates.Status'])),
            ('hot_list', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('appointment_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('linkedin_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('website_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('next_call_back', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('next_step', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('address_1', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('address_2', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('mobile_phone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('business_phone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('home_phone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('other_phone_1', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('other_phone_2', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('other_phone_3', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('phone_ext', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('phone_ext_1', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('phone_ext_2', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('is_primary_contact', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('contact_title', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='contacts', null=True, to=orm['estimates.ContactTitle'])),
            ('contact_title_other', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'estimates', ['Contact'])

        # Adding model 'EstimateType'
        db.create_table(u'estimates_estimatetype', (
            ('estimate_type_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'estimates', ['EstimateType'])

        # Adding model 'ProposalType'
        db.create_table(u'estimates_proposaltype', (
            ('proposal_type_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'estimates', ['ProposalType'])

        # Adding model 'PricingType'
        db.create_table(u'estimates_pricingtype', (
            ('pricing_type_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'estimates', ['PricingType'])

        # Adding model 'AdditionalChargeType'
        db.create_table(u'estimates_additionalchargetype', (
            ('additional_charge_type_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('approval', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'estimates', ['AdditionalChargeType'])

        # Adding model 'PrevailingWage'
        db.create_table(u'estimates_prevailingwage', (
            ('prevailing_wage_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'estimates', ['PrevailingWage'])

        # Adding model 'Contractor'
        db.create_table(u'estimates_contractor', (
            ('contractor_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contractors', to=orm['estimates.Location'])),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contractors', to=orm['estimates.Status'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('vendor_code', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('is_payroll', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('start_pay_period', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('end_pay_period', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('pr_location_code', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('track_lead', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_by', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'estimates', ['Contractor'])

        # Adding model 'Estimate'
        db.create_table(u'estimates_estimate', (
            ('estimate_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='estimates', to=orm['estimates.Customer'])),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='estimates', null=True, on_delete=models.SET_NULL, to=orm['estimates.Status'])),
            ('booking_branch', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='estimates', null=True, on_delete=models.SET_NULL, to=orm['estimates.Location'])),
            ('overtime_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='estimates', null=True, on_delete=models.SET_NULL, to=orm['estimates.OvertimeType'])),
            ('drive_time_code', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='estimates', null=True, on_delete=models.SET_NULL, to=orm['estimates.DriveTimeCode'])),
            ('rate_schedule', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='estimates', null=True, on_delete=models.SET_NULL, to=orm['estimates.RateSchedule'])),
            ('valuation_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='estimates', null=True, on_delete=models.SET_NULL, to=orm['estimates.ValuationType'])),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='estimates', null=True, on_delete=models.SET_NULL, to=orm['estimates.Contact'])),
            ('estimate_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='estimates', null=True, on_delete=models.SET_NULL, to=orm['estimates.EstimateType'])),
            ('proposal_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='estimates', null=True, on_delete=models.SET_NULL, to=orm['estimates.ProposalType'])),
            ('estimate_no', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('job_title', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('contract_no', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('head_count', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('job_rcvd_from', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('job_rcvd_by', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('job_rcvd_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('po_no', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('is_prevailing_wage', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('security_required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('valuation_is_optional', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('consumable_charge_is_optional', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('energy_charge_is_optional', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('instructions', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('square_feet', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cartons', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('crates', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dolly_loads', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('mc_loads', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('bc_loads', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pc_loads', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tub_loads', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('other_loads', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pricing_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='estimates', null=True, on_delete=models.SET_NULL, to=orm['estimates.PricingType'])),
            ('overtime_code', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='estimates', null=True, on_delete=models.SET_NULL, to=orm['estimates.OvertimeCode'])),
            ('consumable_charge_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='consumable_estimates', null=True, on_delete=models.SET_NULL, to=orm['estimates.AdditionalChargeType'])),
            ('energy_charge_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='energy_estimates', null=True, on_delete=models.SET_NULL, to=orm['estimates.AdditionalChargeType'])),
            ('submitted_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('submitted_by', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('approved_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('approved_by', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('confirmed_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('confirmed_by', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('converted_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('converted_by', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('sales_tax_currency', self.gf('djmoney.models.fields.CurrencyField')(default='USD')),
            ('sales_tax', self.gf('djmoney.models.fields.MoneyField')(default_currency='USD', null=True, max_digits=10, decimal_places=2, blank=True)),
            ('consumable_pct', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('energy_charge_pct', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('sales_tax_pct', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('contractor', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='estimates', null=True, on_delete=models.SET_NULL, to=orm['estimates.Contractor'])),
            ('prevailing_wage', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='estimates', null=True, on_delete=models.SET_NULL, to=orm['estimates.PrevailingWage'])),
            ('valuation_amount_currency', self.gf('djmoney.models.fields.CurrencyField')()),
            ('valuation_amount', self.gf('djmoney.models.fields.MoneyField')(default_currency='XYZ', null=True, max_digits=10, decimal_places=2, blank=True)),
        ))
        db.send_create_signal(u'estimates', ['Estimate'])


    def backwards(self, orm):
        # Deleting model 'Status'
        db.delete_table(u'estimates_status')

        # Deleting model 'CustomerType'
        db.delete_table(u'estimates_customertype')

        # Deleting model 'OvertimeType'
        db.delete_table(u'estimates_overtimetype')

        # Deleting model 'DriveTimeCode'
        db.delete_table(u'estimates_drivetimecode')

        # Deleting model 'ValuationType'
        db.delete_table(u'estimates_valuationtype')

        # Deleting model 'PaymentType'
        db.delete_table(u'estimates_paymenttype')

        # Deleting model 'Competitor'
        db.delete_table(u'estimates_competitor')

        # Deleting model 'OvertimeCode'
        db.delete_table(u'estimates_overtimecode')

        # Deleting model 'Location'
        db.delete_table(u'estimates_location')

        # Deleting model 'EffectiveRate'
        db.delete_table(u'estimates_effectiverate')

        # Deleting model 'RateSchedule'
        db.delete_table(u'estimates_rateschedule')

        # Deleting model 'Customer'
        db.delete_table(u'estimates_customer')

        # Deleting model 'ContactTitle'
        db.delete_table(u'estimates_contacttitle')

        # Deleting model 'Contact'
        db.delete_table(u'estimates_contact')

        # Deleting model 'EstimateType'
        db.delete_table(u'estimates_estimatetype')

        # Deleting model 'ProposalType'
        db.delete_table(u'estimates_proposaltype')

        # Deleting model 'PricingType'
        db.delete_table(u'estimates_pricingtype')

        # Deleting model 'AdditionalChargeType'
        db.delete_table(u'estimates_additionalchargetype')

        # Deleting model 'PrevailingWage'
        db.delete_table(u'estimates_prevailingwage')

        # Deleting model 'Contractor'
        db.delete_table(u'estimates_contractor')

        # Deleting model 'Estimate'
        db.delete_table(u'estimates_estimate')


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
            'balance_limit_amt': ('djmoney.models.fields.MoneyField', [], {'default_currency': "'USD'", 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'balance_limit_amt_currency': ('djmoney.models.fields.CurrencyField', [], {'default': "'USD'"}),
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
            'job_limit_amt': ('djmoney.models.fields.MoneyField', [], {'default_currency': "'USD'", 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'job_limit_amt_currency': ('djmoney.models.fields.CurrencyField', [], {'default': "'USD'"}),
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
            'rate': ('djmoney.models.fields.MoneyField', [], {'default_currency': "'USD'", 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'rate_currency': ('djmoney.models.fields.CurrencyField', [], {'default': "'USD'"}),
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
            'sales_tax': ('djmoney.models.fields.MoneyField', [], {'default_currency': "'USD'", 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'sales_tax_currency': ('djmoney.models.fields.CurrencyField', [], {'default': "'USD'"}),
            'sales_tax_pct': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'security_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'square_feet': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'estimates'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['estimates.Status']"}),
            'submitted_by': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'submitted_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'tub_loads': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'valuation_amount': ('djmoney.models.fields.MoneyField', [], {'default_currency': u"'XYZ'", 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'valuation_amount_currency': ('djmoney.models.fields.CurrencyField', [], {}),
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
            'sales_tax': ('djmoney.models.fields.MoneyField', [], {'max_digits': '10', 'decimal_places': '2', 'default_currency': "'USD'"}),
            'sales_tax_currency': ('djmoney.models.fields.CurrencyField', [], {'default': "'USD'"}),
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
            'location_id': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rate_schedules'", 'to': u"orm['estimates.Location']"}),
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