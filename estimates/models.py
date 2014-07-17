from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    sort_order = models.IntegerField()

    def __unicode__(self):
        return u'%s: %s' % (self.type, self.name)

class CustomerType(models.Model):
    customer_type_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    sort_order = models.IntegerField()

    def __unicode__(self):
        return u'%s' % (self.type)

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

class PaymentType(models.Model):
    payment_type_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    sort_order = models.IntegerField()

    def __unicode__(self):
        return u'%s' % (self.code)

class Competitor(models.Model):
    competitor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    created_by = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s: %s' % (self.type, self.name)

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

class ContactTitle(models.Model):
    contact_title_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    created_by = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.title)

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, related_name='contacts')
    status = models.ForeignKey(Status, related_name='contacts', null=True, blank=True)
    hot_list = models.BooleanField(default=False)
    appointment_date = models.DateTimeField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    website_url = models.URLField(null=True, blank=True)
    next_call_back = models.DateTimeField(null=True, blank=True)
    next_step = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address_1 = models.CharField(max_length=250, null=True, blank=True)
    address_2 = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    mobile_phone = models.CharField(max_length=20, null=True, blank=True)
    business_phone = models.CharField(max_length=20, null=True, blank=True)
    home_phone = models.CharField(max_length=20, null=True, blank=True)
    fax = models.CharField(max_length=20, null=True, blank=True)
    other_phone_1 = models.CharField(max_length=20, null=True, blank=True)
    other_phone_2 = models.CharField(max_length=20, null=True, blank=True)
    other_phone_3 = models.CharField(max_length=20, null=True, blank=True)
    phone_ext = models.CharField(max_length=20, null=True, blank=True)
    phone_ext_1 = models.CharField(max_length=20, null=True, blank=True)
    phone_ext_2 = models.CharField(max_length=20, null=True, blank=True)
    is_primary_contact = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)
    sort_order = models.IntegerField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, null=True, blank=True)
    modified_on = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=50, null=True, blank=True)
    contact_title = models.ForeignKey(ContactTitle, related_name='contacts', null=True, blank=True)
    contact_title_other = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

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

class WorkOrderGroup(models.Model):
    work_order_group_id = models.AutoField(primary_key=True)
    estimate = models.ForeignKey(Estimate, related_name='work_order_groups', null=True, blank=True)
    group_name = models.CharField(max_length=50, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    add_to_total = models.BooleanField(default=False)
    group_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sort_order = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, null=True, blank=True)
    modified_on = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return u'%s' % (self.group_name)

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

class ServiceLine(models.Model):
    service_line_id = models.AutoField(primary_key=True)
    service = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    energy_surcharge = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    is_billing = models.BooleanField(default=True)
    is_tl_supported = models.BooleanField(default=True)
    sort_order = models.IntegerField(default=0)
    is_roi = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s' % (self.service)

class WorkOrder(models.Model):
    work_order_id = models.AutoField(primary_key=True)
    work_order_group = models.ForeignKey(WorkOrderGroup, related_name='current_group_work_orders', null=True, blank=True)
    estimate = models.ForeignKey(Estimate, related_name='work_orders', null=True, blank=True)
    #job = models.ForeignKey(Job, related_name='work_orders', null=True, blank=True)
    status = models.ForeignKey(Status, related_name='work_orders', null=True, blank=True)
    work_order_no = models.IntegerField(null=True, blank=True)
    service_date = models.DateTimeField(null=True, blank=True)
    depart_time = models.DateTimeField(null=True, blank=True)
    on_site_time = models.DateTimeField(null=True, blank=True)
    estimated_hours = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    origin_location = models.ForeignKey(CustomerAddress, related_name='origin_work_orders', null=True, blank=True)
    destination_location = models.ForeignKey(CustomerAddress, related_name='destination_work_orders', null=True, blank=True)
    labor_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    packing_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    general_relocation_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    installation_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tech_work_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    material_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    packing_material_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    installation_hardware_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tech_supply_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    unitized_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    storage_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    services_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    original_group = models.ForeignKey(WorkOrderGroup, related_name='original_group_work_orders', null=True, blank=True)
    clone_from = models.CharField(max_length=50, null=True, blank=True)
    clone_date = models.DateTimeField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)
    modified_on = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=100, null=True, blank=True)
    origin_contact = models.ForeignKey(Contact, related_name='origin_contact_work_orders', null=True, blank=True)
    destination_contact = models.ForeignKey(Contact, related_name='destination_contact_work_orders', null=True, blank=True)
    service_line = models.ForeignKey(ServiceLine, related_name='work_orders', null=True, blank=True)
    depart_military_time = models.CharField(max_length=4, null=True, blank=True)
    on_site_military_time = models.CharField(max_length=4, null=True, blank=True)
    service_branch = models.ForeignKey(Location, related_name='work_orders', null=True, blank=True)

    def __unicode__(self):
        return u'%s: %s' % (self.estimate.estimate_no, self.work_order_no)

class WorkOrderComment(models.Model):
    work_order_comment_id = models.AutoField(primary_key=True)
    work_order = models.ForeignKey(WorkOrder, related_name='work_order_comments')
    comment = models.TextField(default='')
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, default='admin')
    sort_order = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % (self.work_order_comment_id)

class EquipmentItem(models.Model):
    equipment_item_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    is_inventory_item = models.BooleanField(default=False)
    is_default = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    sort_order = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % (self.code)

class InstallationService(models.Model):
    installation_service_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    minutes_to_install = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, default='admin')
    sort_order = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % (self.code)

class LaborCategory(models.Model):
    labor_category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    sort_order = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % (self.category)

class LaborTask(models.Model):
    labor_task_id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    sort_order = models.IntegerField(default=0)
    labor_category = models.ForeignKey(LaborCategory, related_name='labor_tasks', null=True, blank=True)

    def __unicode__(self):
        return u'%s' % (self.task)

class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    is_default = models.BooleanField(default=False)
    category = models.CharField(max_length=50)
    minutes_to_pack = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, default='admin')

    def __unicode__(self):
        return u'%s' % (self.code)

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

class Unit(models.Model):
    unit_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    unit_of_measure = models.CharField(max_length=50)
    unit_type = models.IntegerField(null=True, blank=True)
    category = models.CharField(max_length=50)
    minutes_per_unit = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, default='admin')

    def __unicode__(self):
        return u'%s' % (self.code)

class WorkOrderEquipmentItem(models.Model):
    work_order_equipment_item_id = models.AutoField(primary_key=True)
    work_order = models.ForeignKey(WorkOrder, related_name='work_order_equipment_items')
    equipment_item = models.ForeignKey(EquipmentItem, related_name='work_order_equipment_items')
    quantity = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, default='admin')
    modified_on = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=50, default='admin')
    sort_order = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % (self.work_order_equipment_item_id)

class WorkOrderInstallService(models.Model):
    work_order_install_service_id = models.AutoField(primary_key=True)
    work_order = models.ForeignKey(WorkOrder, related_name='work_order_install_services')
    installation_service = models.ForeignKey(InstallationService, related_name='work_order_install_services')
    quantity = models.IntegerField(default=0)
    shifts = models.IntegerField(default=0)
    men = models.IntegerField(default=0)
    man_hours = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    travel_time = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    crew_hours = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rt_hours = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ot_hours = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pt_hours = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, default='admin')
    modified_on = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=50, default='admin')
    sort_order = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % (self.work_order_install_service_id)

class WorkOrderLaborTask(models.Model):
    work_order_labor_task_id = models.AutoField(primary_key=True)
    work_order = models.ForeignKey(WorkOrder, related_name='work_order_labor_tasks')
    labor_task = models.ForeignKey(LaborTask, related_name='work_order_labor_tasks')
    quantity = models.IntegerField(default=0)
    total_hours = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    reg_hours = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    reg_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ot_hours = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ot_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pt_hours = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pt_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, default='admin')
    modified_on = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=50, default='admin')
    sort_order = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % (self.work_order_labor_task_id)

class WorkOrderMaterial(models.Model):
    work_order_material_id = models.AutoField(primary_key=True)
    work_order = models.ForeignKey(WorkOrder, related_name='work_order_materials')
    material = models.ForeignKey(Material, related_name='work_order_materials')
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, default='admin')
    modified_on = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=50, default='admin')
    sort_order = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % (self.work_order_material_id)

class WorkOrderUnit(models.Model):
    work_order_unit_id = models.AutoField(primary_key=True)
    work_order = models.ForeignKey(WorkOrder, related_name='work_order_units')
    unit = models.ForeignKey(Unit, related_name='work_order_units')
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, default='admin')
    modified_on = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=50, default='admin')
    sort_order = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % (self.work_order_unit_id)

class WorkOrderVehicle(models.Model):
    work_order_vehicle_id = models.AutoField(primary_key=True)
    work_order = models.ForeignKey(WorkOrder, related_name='work_order_vehicles')
    vehicle_type = models.ForeignKey(VehicleType, related_name='work_order_vehicles')
    quantity = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, default='admin')
    modified_on = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=50, default='admin')
    sort_order = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % (self.work_order_vehicle_id)
