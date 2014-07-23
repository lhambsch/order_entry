from rest_framework import serializers
from ..models import (VehicleType, OvertimeType, DriveTimeCode, ValuationType, Status, Location, Contractor,
    EffectiveRate, OvertimeCode, PaymentType, RateSchedule)


class VehicleTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleType

class OvertimeTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = OvertimeType

class DriveTimeCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DriveTimeCode

class ValuationTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ValuationType

class OvertimeCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = OvertimeCode

class PaymentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentType

class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status

class LocationSerializer(serializers.ModelSerializer):
    customers = serializers.HyperlinkedIdentityField('customers', view_name='location_customer_list', lookup_field='location')
    estimates = serializers.HyperlinkedIdentityField('estimates', view_name='location_estimate_list', lookup_field='location')

    class Meta:
        model = Location

class ContractorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contractor

class EffectiveRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = EffectiveRate

class RateScheduleSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    effective_rate = EffectiveRateSerializer()

    class Meta:
        model = RateSchedule
