from rest_framework import serializers
from estimates import models


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Status

class CustomerTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomerType

class OvertimeTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.OvertimeType

class DriveTimeCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DriveTimeCode

class ValuationTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ValuationType

class PaymentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PaymentType

class CompetitorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Competitor

class OvertimeCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.OvertimeCode

class LocationSerializer(serializers.ModelSerializer):
    customers = serializers.HyperlinkedIdentityField('customers', view_name='location_customer_list', lookup_field='location')
    estimates = serializers.HyperlinkedIdentityField('estimates', view_name='location_estimate_list', lookup_field='location')

    class Meta:
        model = models.Location

class EffectiveRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.EffectiveRate

class RateScheduleSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    effective_rate = EffectiveRateSerializer()

    class Meta:
        model = models.RateSchedule

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
        model = models.Customer

class ContactTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ContactTitle

class ContactSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    status = StatusSerializer(required=False)
    contact_title = ContactTitleSerializer()

    class Meta:
        model = models.Contact

class EstimateTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.EstimateType

class ProposalTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProposalType

class PricingTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PricingType

class AdditionalChargeTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AdditionalChargeType

class PrevailingWageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PrevailingWage

class ContractorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Contractor

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
        model = models.Estimate

class WorkOrderGroupSerializer(serializers.ModelSerializer):
    estimate = EstimateSerializer(required=False)

    class Meta:
        model = models.WorkOrderGroup

class CustomerAddressSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(required=False)

    class Meta:
        model = models.CustomerAddress

class ServiceLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ServiceLine

class WorkOrderSerializer(serializers.ModelSerializer):
    work_order_group = WorkOrderGroupSerializer(required=False)
    estimate = EstimateSerializer(required=False)
    status = StatusSerializer(required=False)
    origin_location = CustomerAddressSerializer(required=False)
    destination_location = CustomerAddressSerializer(required=False)
    original_group = WorkOrderGroupSerializer(required=False)
    origin_contact = ContactSerializer(required=False)
    destination_contact = ContactSerializer(required=False)
    service_line = ServiceLineSerializer(required=False)
    service_branch = LocationSerializer(required=False)

    work_order_comments = serializers.HyperlinkedIdentityField('work_order_comments', view_name='workorder_workordercomments_list', lookup_field='work_order')
    work_order_equipment_items = serializers.HyperlinkedIdentityField('work_order_equipment_items', view_name='workorder_workorderequipmentitems_list', lookup_field='work_order')
    work_order_install_services = serializers.HyperlinkedIdentityField('work_order_install_services', view_name='workorder_workorderinstallservices_list', lookup_field='work_order')
    work_order_labor_tasks = serializers.HyperlinkedIdentityField('work_order_labor_tasks', view_name='workorder_workorderlabortasks_list', lookup_field='work_order')
    work_order_materials = serializers.HyperlinkedIdentityField('work_order_materials', view_name='workorder_workordermaterials_list', lookup_field='work_order')
    work_order_units = serializers.HyperlinkedIdentityField('work_order_units', view_name='workorder_workorderunits_list', lookup_field='work_order')
    work_order_vehicles = serializers.HyperlinkedIdentityField('work_order_vehicles', view_name='workorder_workordervehicles_list', lookup_field='work_order')

    class Meta:
        model = models.WorkOrder

class WorkOrderCommentSerializer(serializers.ModelSerializer):
    work_order = WorkOrderSerializer()

    class Meta:
        model = models.WorkOrderComment

class EquipmentItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.EquipmentItem

class InstallationServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.InstallationService

class LaborCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LaborCategory

class LaborTaskSerializer(serializers.ModelSerializer):
    labor_category = LaborCategorySerializer()

    class Meta:
        model = models.LaborTask

class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Material

class VehicleTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.VehicleType

class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Unit

class WorkOrderEquipmentItemSerializer(serializers.ModelSerializer):
    work_order = WorkOrderSerializer()
    equipment_item = EquipmentItemSerializer()

    class Meta:
        model = models.WorkOrderEquipmentItem

class WorkOrderInstallServiceSerializer(serializers.ModelSerializer):
    work_order = WorkOrderSerializer()
    installation_service = InstallationServiceSerializer()

    class Meta:
        model = models.WorkOrderInstallService

class WorkOrderLaborTaskSerializer(serializers.ModelSerializer):
    work_order = WorkOrderSerializer()
    labor_task = LaborTaskSerializer()

    class Meta:
        model = models.WorkOrderLaborTask

class WorkOrderMaterialSerializer(serializers.ModelSerializer):
    work_order = WorkOrderSerializer()
    material = MaterialSerializer()

    class Meta:
        model = models.WorkOrderMaterial

class WorkOrderUnitSerializer(serializers.ModelSerializer):
    work_order = WorkOrderSerializer()
    unit = UnitSerializer()

    class Meta:
        model = models.WorkOrderUnit

class WorkOrderVehicleSerializer(serializers.ModelSerializer):
    work_order = WorkOrderSerializer()
    vehicle_type = VehicleTypeSerializer()

    class Meta:
        model = models.WorkOrderVehicle

