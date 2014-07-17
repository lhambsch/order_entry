from django.db import models


class CustomerType(models.Model):
    customer_type_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    sort_order = models.IntegerField()

    def __unicode__(self):
        return u'%s' % (self.type)

class Competitor(models.Model):
    competitor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    created_by = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s: %s' % (self.type, self.name)

class CustomerAddress(models.Model):
    customer_address_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, related_name='customer_addresses', null=True, blank=True)
    location_name = models.CharField(max_length=50, null=True, blank=True)
    street_1 = models.CharField(max_length=31, null=True, blank=True)
    street_2 = models.CharField(max_length=31, null=True, blank=True)
    city = models.CharField(max_length=31, null=True, blank=True)
    state = models.CharField(max_length=29, null=True, blank=True)
    zip_code = models.CharField(max_length=14, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, null=True, blank=True)
    modified_on = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return u'%s: %s' % (self.customer.customer_name, self.location_name)

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    parent_customer = models.ForeignKey('self', related_name='children', null=True, blank=True)
    customer_type = models.ForeignKey(CustomerType, related_name='customers', null=True, blank=True)
    overtime_type = models.ForeignKey(OvertimeType, related_name='customers', null=True, blank=True)
    drive_time_code = models.ForeignKey(DriveTimeCode, related_name='customers', null=True, blank=True)
    status = models.ForeignKey(Status, related_name='customers', null=True, blank=True)
    valuation_type = models.ForeignKey(ValuationType, related_name='customers', null=True, blank=True)
    payment_type = models.ForeignKey(PaymentType, related_name='customers', null=True, blank=True)
    customer_name = models.CharField(max_length=100)
    customer_code = models.CharField(max_length=100)
    customer_no = models.CharField(max_length=20, null=True, blank=True)
    exempt_sales_tax = models.BooleanField(default=False)
    exempt_equipment_load_time = models.BooleanField(default=False)
    is_prevailing_wage = models.BooleanField(default=False)
    exempt_energy_charge = models.BooleanField(default=False)
    exempt_consumable_supply = models.BooleanField(default=False)
    address_1 = models.CharField(max_length=200, null=True, blank=True)
    address_2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    balance_limit_amt = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    job_limit_amt = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    modified_on = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=100, null=True, blank=True)
    energy_charge_percentage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    consumable_charge_percentage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    great_plains_name = models.CharField(max_length=255, null=True, blank=True)
    last_credit_check = models.DateTimeField(null=True, blank=True)
    terms_and_conditions = models.DateTimeField(null=True, blank=True)
    website_url = models.URLField(null=True, blank=True)
    furniture_competitor = models.ForeignKey(Competitor, related_name='furniture_customers', null=True, blank=True)
    furniture_competitor_other = models.CharField(max_length=255, null=True, blank=True)
    installation_competitor = models.ForeignKey(Competitor, related_name='installation_customers', null=True, blank=True)
    installation_competitor_other = models.CharField(max_length=255, null=True, blank=True)
    warehouse_competitor = models.ForeignKey(Competitor, related_name='warehouse_customers', null=True, blank=True)
    warehouse_competitor_other = models.CharField(max_length=255, null=True, blank=True)
    tech_competitor = models.ForeignKey(Competitor, related_name='tech_customers', null=True, blank=True)
    tech_competitor_other = models.CharField(max_length=255, null=True, blank=True)
    logistics_competitor = models.ForeignKey(Competitor, related_name='logistics_customers', null=True, blank=True)
    logistics_competitor_other = models.CharField(max_length=255, null=True, blank=True)
    moving_competitor = models.ForeignKey(Competitor, related_name='moving_customers', null=True, blank=True)
    moving_competitor_other = models.CharField(max_length=255, null=True, blank=True)
    is_prospect = models.BooleanField(default=False)
    overtime_code = models.ForeignKey(OvertimeCode, related_name='customers', null=True, blank=True)
    hot_list = models.BooleanField(default=False)
    is_roi_prospect = models.BooleanField(default=False)
    bill_customer_name = models.CharField(max_length=100, null=True, blank=True)
    bill_attn_name = models.CharField(max_length=100, null=True, blank=True)
    bill_address_1 = models.CharField(max_length=100, null=True, blank=True)
    bill_address_2 = models.CharField(max_length=100, null=True, blank=True)
    bill_city = models.CharField(max_length=100, null=True, blank=True)
    bill_state = models.CharField(max_length=100, null=True, blank=True)
    bill_zip = models.CharField(max_length=50, null=True, blank=True)
    bill_phone = models.CharField(max_length=50, null=True, blank=True)
    bill_phone_ext = models.CharField(max_length=50, null=True, blank=True)
    bill_fax = models.CharField(max_length=50, null=True, blank=True)
    bill_email = models.CharField(max_length=50, null=True, blank=True)
    bill_notes = models.TextField(null=True, blank=True)
    rate_schedule = models.ForeignKey(RateSchedule, related_name='customers', null=True, blank=True)
    location = models.ForeignKey(Location, related_name='customers', null=True, blank=True)
    is_web_order = models.BooleanField(default=False)
    is_cov_u = models.BooleanField(default=False)
    show_consumable = models.BooleanField(default=False)
    show_energy_charge = models.BooleanField(default=False)
    employee_count = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return u'%s' % (self.customer_name)
