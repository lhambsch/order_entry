from rest_framework import serializers

from ..models import CustomerType, Customer, CustomerAddress, Competitor


class CustomerTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerType

class CompetitorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Competitor

class CustomerSerializer(serializers.ModelSerializer):
    customer_type = CustomerTypeSerializer(required=False)
    overtime_type = OvertimeTypeSerializer(required=False)
    drive_time_code = DriveTimeCodeSerializer(required=False)
    status = StatusSerializer(required=False)
    valuation_type = ValuationTypeSerializer(required=False)
    payment_type = PaymentTypeSerializer(required=False)
    overtime_code = OvertimeCodeSerializer(required=False)
    rate_schedule = RateScheduleSerializer(required=False)
    location = LocationSerializer(required=False)
    contacts = serializers.HyperlinkedIdentityField('contacts', view_name='customer_contact_list', lookup_field='customer')

    class Meta:
        model = Customer

class CustomerAddressSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(required=False)

    class Meta:
        model = CustomerAddress
