from django.db import models


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
