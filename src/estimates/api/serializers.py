from rest_framework import serializers
from ..models import (Estimate)


class EstimateTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EstimateType

class ProposalTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProposalType

class PricingTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PricingType

class AdditionalChargeTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdditionalChargeType

class PrevailingWageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PrevailingWage

class EstimateSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(required=False)
    status = StatusSerializer(required=False)
    booking_branch = LocationSerializer(required=False)
    overtime_type = OvertimeTypeSerializer(required=False)
    drive_time_code = DriveTimeCodeSerializer(required=False)
    rate_schedule = RateScheduleSerializer(required=False)
    valuation_type = ValuationTypeSerializer(required=False)
    contact = ContactSerializer(required=False)
    estimate_type = EstimateTypeSerializer(required=False)
    proposal_type = ProposalTypeSerializer(required=False)
    pricing_type = PricingTypeSerializer(required=False)
    overtime_code = OvertimeCodeSerializer(required=False)
    consumable_charge_type = AdditionalChargeTypeSerializer(required=False)
    energy_charge_type = AdditionalChargeTypeSerializer(required=False)
    contractor = ContractorSerializer(required=False)
    prevailing_wage = PrevailingWageSerializer(required=False)

    work_orders = serializers.HyperlinkedIdentityField('work_orders', view_name='estimate_workorder_list', lookup_field='estimate')

    class Meta:
        model = Estimate
