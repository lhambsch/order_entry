from rest_framework import serializers
from ..models import (WorkOrderGroup, ServiceLine, WorkOrder, WorkOrderComment, EquipmentItem, InstallationService,
    LaborCategory, LaborTask, Material, Unit, WorkOrderEquipmentItem, WorkOrderInstallService, WorkOrderLaborTask,
    WorkOrderMaterial, WorkOrderUnit, WorkOrderVehicle)


class WorkOrderGroupSerializer(serializers.ModelSerializer):
    estimate = EstimateSerializer(required=False)

    class Meta:
        model = WorkOrderGroup

class ServiceLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceLine

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
        model = WorkOrder

class WorkOrderCommentSerializer(serializers.ModelSerializer):
    work_order = WorkOrderSerializer()

    class Meta:
        model = WorkOrderComment

class EquipmentItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = EquipmentItem

class InstallationServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = InstallationService

class LaborCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = LaborCategory

class LaborTaskSerializer(serializers.ModelSerializer):
    labor_category = LaborCategorySerializer()

    class Meta:
        model = LaborTask

class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Material

class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unit

class WorkOrderEquipmentItemSerializer(serializers.ModelSerializer):
    work_order = WorkOrderSerializer()
    equipment_item = EquipmentItemSerializer()

    class Meta:
        model = WorkOrderEquipmentItem

class WorkOrderInstallServiceSerializer(serializers.ModelSerializer):
    work_order = WorkOrderSerializer()
    installation_service = InstallationServiceSerializer()

    class Meta:
        model = WorkOrderInstallService

class WorkOrderLaborTaskSerializer(serializers.ModelSerializer):
    work_order = WorkOrderSerializer()
    labor_task = LaborTaskSerializer()

    class Meta:
        model = WorkOrderLaborTask

class WorkOrderMaterialSerializer(serializers.ModelSerializer):
    work_order = WorkOrderSerializer()
    material = MaterialSerializer()

    class Meta:
        model = WorkOrderMaterial

class WorkOrderUnitSerializer(serializers.ModelSerializer):
    work_order = WorkOrderSerializer()
    unit = UnitSerializer()

    class Meta:
        model = WorkOrderUnit

class WorkOrderVehicleSerializer(serializers.ModelSerializer):
    work_order = WorkOrderSerializer()
    vehicle_type = VehicleTypeSerializer()

    class Meta:
        model = WorkOrderVehicle
