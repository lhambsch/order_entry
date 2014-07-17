from django.db import models
from django.contrib.auth.models import User

from customers.models import Customer
from contacts.models import Contact
from common.models import (Status, Location, OvertimeType, DriveTimeCode, RateSchedule, ValuationType,
    PricingType, OvertimeCode, AdditionalChargeType)

class EstimateType(models.Model):
    estimate_type_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)
    sort_order = models.IntegerField()

    def __unicode__(self):
        return u'%s' % (self.type)

class ProposalType(models.Model):
    proposal_type_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    sort_order = models.IntegerField()

    def __unicode__(self):
        return u'%s' % (self.type)

class PricingType(models.Model):
    pricing_type_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    sort_order = models.IntegerField()

    def __unicode__(self):
        return u'%s: %s' % (self.type, self.code)

class AdditionalChargeType(models.Model):
    additional_charge_type_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    approval = models.BooleanField(default=False)
    sort_order = models.IntegerField()

    def __unicode__(self):
        return u'%s: %s' % (self.type, self.category)

class PrevailingWage(models.Model):
    prevailing_wage_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)
    code = models.CharField(max_length=10, null=True, blank=True)
    sort_order = models.IntegerField()

    def __unicode__(self):
        return u'%s' % (self.description)

class Estimate(models.Model):
    estimate_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, related_name='estimates')
    status = models.ForeignKey(Status, related_name='estimates', null=True, blank=True, on_delete=models.SET_NULL)
    booking_branch = models.ForeignKey(Location, related_name='estimates', null=True, blank=True, on_delete=models.SET_NULL)
    overtime_type = models.ForeignKey(OvertimeType, related_name='estimates', null=True, blank=True, on_delete=models.SET_NULL)
    drive_time_code = models.ForeignKey(DriveTimeCode, related_name='estimates', null=True, blank=True, on_delete=models.SET_NULL)
    rate_schedule = models.ForeignKey(RateSchedule, related_name='estimates', null=True, blank=True, on_delete=models.SET_NULL)
    valuation_type = models.ForeignKey(ValuationType, related_name='estimates', null=True, blank=True, on_delete=models.SET_NULL)
    contact = models.ForeignKey(Contact, related_name='estimates', null=True, blank=True, on_delete=models.SET_NULL)
    estimate_type = models.ForeignKey(EstimateType, related_name='estimates', null=True, blank=True, on_delete=models.SET_NULL)
    proposal_type = models.ForeignKey(ProposalType, related_name='estimates', null=True, blank=True, on_delete=models.SET_NULL)
    estimate_no = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50, null=True, blank=True)
    contract_no = models.CharField(max_length=20, null=True, blank=True)
    head_count = models.IntegerField(null=True, blank=True)
    job_rcvd_from = models.CharField(max_length=20, null=True, blank=True)
    job_rcvd_by = models.CharField(max_length=20, null=True, blank=True)
    job_rcvd_date = models.DateTimeField(null=True, blank=True)
    po_no = models.CharField(max_length=20, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    is_prevailing_wage = models.BooleanField(default=False)
    security_required = models.BooleanField(default=False)
    valuation_is_optional = models.BooleanField(default=False)
    consumable_charge_is_optional = models.BooleanField(default=False)
    energy_charge_is_optional = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    modified_on = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    square_feet = models.IntegerField(null=True, blank=True)
    cartons = models.IntegerField(null=True, blank=True)
    crates = models.IntegerField(null=True, blank=True)
    dolly_loads = models.IntegerField(null=True, blank=True)
    mc_loads = models.IntegerField(null=True, blank=True)
    bc_loads = models.IntegerField(null=True, blank=True)
    pc_loads = models.IntegerField(null=True, blank=True)
    tub_loads = models.IntegerField(null=True, blank=True)
    other_loads = models.IntegerField(null=True, blank=True)
    pricing_type = models.ForeignKey(PricingType, related_name='estimates', null=True, blank=True, on_delete=models.SET_NULL)
    overtime_code = models.ForeignKey(OvertimeCode, related_name='estimates', null=True, blank=True, on_delete=models.SET_NULL)
    consumable_charge_type = models.ForeignKey(AdditionalChargeType, related_name='consumable_estimates', null=True, blank=True, on_delete=models.SET_NULL)
    energy_charge_type = models.ForeignKey(AdditionalChargeType, related_name='energy_estimates', null=True, blank=True, on_delete=models.SET_NULL)
    submitted_on = models.DateTimeField(null=True, blank=True)
    submitted_by = models.CharField(max_length=100, null=True, blank=True)
    approved_on = models.DateTimeField(null=True, blank=True)
    approved_by = models.CharField(max_length=100, null=True, blank=True)
    confirmed_on = models.DateTimeField(null=True, blank=True)
    confirmed_by = models.CharField(max_length=100, null=True, blank=True)
    converted_on = models.DateTimeField(null=True, blank=True)
    converted_by = models.CharField(max_length=100, null=True, blank=True)
    sales_tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    consumable_pct = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    energy_charge_pct = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sales_tax_pct = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    contractor = models.ForeignKey(Contractor, related_name='estimates', null=True, blank=True, on_delete=models.SET_NULL)
    prevailing_wage = models.ForeignKey(PrevailingWage, related_name='estimates', null=True, blank=True, on_delete=models.SET_NULL)
    valuation_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __unicode__(self):
        return u'%s' % (self.estimate_no)
