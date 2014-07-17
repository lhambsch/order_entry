from django.db import models


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
