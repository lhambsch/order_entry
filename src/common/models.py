from django.db import models


class VehicleType(models.Model):
    vehicle_type_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    is_inventory_item = models.BooleanField(default=False)
    is_default = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    sort_order = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % (self.code)

class OvertimeType(models.Model):
    overtime_type_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    sort_order = models.IntegerField()

    def __unicode__(self):
        return u'%s' % (self.code)

class DriveTimeCode(models.Model):
    drive_time_code_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=50, null=True, blank=True)
    sort_order = models.IntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __unicode__(self):
        return u'%s' % (self.code)

class ValuationType(models.Model):
    valuation_type_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    rpt_description = models.CharField(max_length=255)
    weight = models.IntegerField(null=True, blank=True)
    is_flat_fee = models.BooleanField(default=False)
    factor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sort_order = models.IntegerField()

    def __unicode__(self):
        return u'%s' % (self.code)

class OvertimeCode(models.Model):
    overtime_code_id = models.AutoField(primary_key=True)
    overtime_type = models.ForeignKey(OvertimeType, related_name='overtime_codes')
    description = models.CharField(max_length=150)
    code = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    overtime = models.IntegerField(null=True, blank=True)
    premium_time = models.IntegerField(null=True, blank=True)
    time_in = models.IntegerField(null=True, blank=True)
    time_out = models.IntegerField(null=True, blank=True)
    sort_order = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return u'%s' % (self.code)

class PaymentType(models.Model):
    payment_type_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    sort_order = models.IntegerField()

    def __unicode__(self):
        return u'%s' % (self.code)

class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    sort_order = models.IntegerField()

    def __unicode__(self):
        return u'%s: %s' % (self.type, self.name)

class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    job_no_prefix = models.CharField(max_length=50)
    sales_tax = models.DecimalField(max_digits=10, decimal_places=2)
    is_terminal = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_service_branch = models.BooleanField(default=False)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    fax = models.CharField(max_length=20, null=True, blank=True)

    def __unicode__(self):
        return u'%s' % (self.code)

class Contractor(models.Model):
    contractor_id = models.AutoField(primary_key=True)
    location = models.ForeignKey(Location, related_name='contractors')
    status = models.ForeignKey(Status, related_name='contractors')
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50, null=True, blank=True)
    vendor_code = models.CharField(max_length=20, null=True, blank=True)
    is_payroll = models.BooleanField(default=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    start_pay_period = models.CharField(max_length=20, null=True, blank=True)
    end_pay_period = models.CharField(max_length=20, null=True, blank=True)
    pr_location_code = models.CharField(max_length=20, null=True, blank=True)
    track_lead = models.BooleanField(default=True)
    created_by = models.CharField(max_length=20, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=20, null=True, blank=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % (self.code)

class EffectiveRate(models.Model):
    effective_rate_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    effective_date = models.DateTimeField(null=True, blank=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return u'%s' % (self.description)

class RateSchedule(models.Model):
    rate_schedule_id = models.AutoField(primary_key=True)
    location = models.ForeignKey(Location, related_name='rate_schedules', default=1, null=True, blank=True)
    effective_rate = models.ForeignKey(EffectiveRate, related_name='rate_schedules', default=1, null=True, blank=True)
    code = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    effective_date = models.DateTimeField(null=True, blank=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    sort_order = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, null=True, blank=True)
    requires_approval = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % (self.code)
