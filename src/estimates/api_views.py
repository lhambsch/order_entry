from rest_framework import generics, permissions

from . import serializers
from estimates import models


class StatusList(generics.ListCreateAPIView):
    model = models.Status
    serializer_class = serializers.StatusSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.Status
    lookup_field = 'status_id'
    serializer_class = serializers.StatusSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class CustomerTypeList(generics.ListCreateAPIView):
    model = models.CustomerType
    serializer_class = serializers.CustomerTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class CustomerTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.CustomerType
    lookup_field = 'customer_type_id'
    serializer_class = serializers.CustomerTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class OvertimeTypeList(generics.ListCreateAPIView):
    model = models.OvertimeType
    serializer_class = serializers.OvertimeTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class OvertimeTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.OvertimeType
    lookup_field = 'overtime_type_id'
    serializer_class = serializers.OvertimeTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class DriveTimeCodeList(generics.ListCreateAPIView):
    model = models.DriveTimeCode
    serializer_class = serializers.DriveTimeCodeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class DriveTimeCodeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.DriveTimeCode
    lookup_field = 'drive_time_code_id'
    serializer_class = serializers.DriveTimeCodeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class ValuationTypeList(generics.ListCreateAPIView):
    model = models.ValuationType
    serializer_class = serializers.ValuationTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class ValuationTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.ValuationType
    lookup_field = 'valuation_type_id'
    serializer_class = serializers.ValuationTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class PaymentTypeList(generics.ListCreateAPIView):
    model = models.PaymentType
    serializer_class = serializers.PaymentTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class PaymentTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.PaymentType
    lookup_field = 'payment_type_id'
    serializer_class = serializers.PaymentTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class CompetitorList(generics.ListCreateAPIView):
    model = models.Competitor
    serializer_class = serializers.CompetitorSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class CompetitorDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.Competitor
    lookup_field = 'competitor_id'
    serializer_class = serializers.CompetitorSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class OvertimeCodeList(generics.ListCreateAPIView):
    model = models.OvertimeCode
    serializer_class = serializers.OvertimeCodeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class OvertimeCodeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.OvertimeCode
    lookup_field = 'overtime_code_id'
    serializer_class = serializers.OvertimeCodeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class LocationList(generics.ListCreateAPIView):
    model = models.Location
    serializer_class = serializers.LocationSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.Location
    lookup_field = 'location_id'
    serializer_class = serializers.LocationSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class LocationCustomerList(generics.ListAPIView):
    model = models.Customer
    serializer_class = serializers.CustomerSerializer

    def get_queryset(self):
        queryset = super(LocationCustomerList, self).get_queryset()
        return queryset.filter(location__location_id=self.kwargs.get('location_id'))

class LocationEstimateList(generics.ListAPIView):
    model = models.Estimate
    serializer_class = serializers.EstimateSerializer

    def get_queryset(self):
        queryset = super(LocationEstimateList, self).get_queryset()
        return queryset.filter(booking_branch__location_id=self.kwargs.get('location_id'))

class EffectiveRateList(generics.ListCreateAPIView):
    model = models.EffectiveRate
    serializer_class = serializers.EffectiveRateSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class EffectiveRateDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.EffectiveRate
    lookup_field = 'effective_rate_id'
    serializer_class = serializers.EffectiveRateSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class RateScheduleList(generics.ListCreateAPIView):
    model = models.RateSchedule
    serializer_class = serializers.RateScheduleSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class RateScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.RateSchedule
    lookup_field = 'rate_schedule_id'
    serializer_class = serializers.RateScheduleSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class CustomerList(generics.ListCreateAPIView):
    model = models.Customer
    serializer_class = serializers.CustomerSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.Customer
    lookup_field = 'customer_id'
    serializer_class = serializers.CustomerSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class CustomerContactList(generics.ListAPIView):
    model = models.Contact
    serializer_class = serializers.ContactSerializer

    def get_queryset(self):
        queryset = super(CustomerContactList, self).get_queryset()
        return queryset.filter(customer__customer_id=self.kwargs.get('customer_id'))

class ContactTitleList(generics.ListCreateAPIView):
    model = models.ContactTitle
    serializer_class = serializers.ContactTitleSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class ContactTitleDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.ContactTitle
    lookup_field = 'contact_title_id'
    serializer_class = serializers.ContactTitleSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class ContactList(generics.ListCreateAPIView):
    model = models.Contact
    serializer_class = serializers.ContactSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.Contact
    lookup_field = 'contact_id'
    serializer_class = serializers.ContactSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class EstimateTypeList(generics.ListCreateAPIView):
    model = models.EstimateType
    serializer_class = serializers.EstimateTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class EstimateTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.EstimateType
    lookup_field = 'estimate_type_id'
    serializer_class = serializers.EstimateTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class ProposalTypeList(generics.ListCreateAPIView):
    model = models.ProposalType
    serializer_class = serializers.ProposalTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class ProposalTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.ProposalType
    lookup_field = 'proposal_type_id'
    serializer_class = serializers.ProposalTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class PricingTypeList(generics.ListCreateAPIView):
    model = models.PricingType
    serializer_class = serializers.PricingTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class PricingTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.PricingType
    lookup_field = 'pricing_type_id'
    serializer_class = serializers.PricingTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class AdditionalChargeTypeList(generics.ListCreateAPIView):
    model = models.AdditionalChargeType
    serializer_class = serializers.AdditionalChargeTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class AdditionalChargeTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.AdditionalChargeType
    lookup_field = 'additional_charge_type_id'
    serializer_class = serializers.AdditionalChargeTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class PrevailingWageList(generics.ListCreateAPIView):
    model = models.PrevailingWage
    serializer_class = serializers.PrevailingWageSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class PrevailingWageDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.PrevailingWage
    lookup_field = 'prevailing_wage_id'
    serializer_class = serializers.PrevailingWageSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class ContractorList(generics.ListCreateAPIView):
    model = models.Contractor
    serializer_class = serializers.ContractorSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class ContractorDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.Contractor
    lookup_field = 'contractor_id'
    serializer_class = serializers.ContractorSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class EstimateList(generics.ListCreateAPIView):
    model = models.Estimate
    serializer_class = serializers.EstimateSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class EstimateDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.Estimate
    lookup_field = 'estimate_id'
    serializer_class = serializers.EstimateSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class EstimateWorkOrderList(generics.ListAPIView):
    model = models.WorkOrder
    serializer_class = serializers.WorkOrderSerializer

    def get_queryset(self):
        queryset = super(EstimateWorkOrderList, self).get_queryset()
        return queryset.filter(estimate__estimate_id=self.kwargs.get('estimate_id'))

class WorkOrderGroupList(generics.ListCreateAPIView):
    model = models.WorkOrderGroup
    serializer_class = serializers.WorkOrderGroupSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.WorkOrderGroup
    lookup_field = 'work_order_group_id'
    serializer_class = serializers.WorkOrderGroupSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class CustomerAddressList(generics.ListCreateAPIView):
    model = models.CustomerAddress
    serializer_class = serializers.CustomerAddressSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class CustomerAddressDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.CustomerAddress
    lookup_field = 'customer_address_id'
    serializer_class = serializers.CustomerAddressSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class ServiceLineList(generics.ListCreateAPIView):
    model = models.ServiceLine
    serializer_class = serializers.ServiceLineSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class ServiceLineDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.ServiceLine
    lookup_field = 'service_line_id'
    serializer_class = serializers.ServiceLineSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderList(generics.ListCreateAPIView):
    model = models.WorkOrder
    serializer_class = serializers.WorkOrderSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.WorkOrder
    lookup_field = 'work_order_id'
    serializer_class = serializers.WorkOrderSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderWorkOrderCommentsList(generics.ListAPIView):
    model = models.WorkOrderComment
    serializer_class = serializers.WorkOrderCommentSerializer

    def get_queryset(self):
        queryset = super(WorkOrderWorkOrderCommentsList, self).get_queryset()
        return queryset.filter(work_order__work_order_id=self.kwargs.get('work_order_id'))

class WorkOrderWorkOrderEquipmentItemsList(generics.ListAPIView):
    model = models.WorkOrderEquipmentItem
    serializer_class = serializers.WorkOrderEquipmentItemSerializer

    def get_queryset(self):
        queryset = super(WorkOrderWorkOrderEquipmentItemsList, self).get_queryset()
        return queryset.filter(work_order__work_order_id=self.kwargs.get('work_order_id'))

class WorkOrderWorkOrderInstallServicesList(generics.ListAPIView):
    model = models.WorkOrderInstallService
    serializer_class = serializers.WorkOrderInstallServiceSerializer

    def get_queryset(self):
        queryset = super(WorkOrderWorkOrderInstallServicesList, self).get_queryset()
        return queryset.filter(work_order__work_order_id=self.kwargs.get('work_order_id'))

class WorkOrderWorkOrderLaborTasksList(generics.ListAPIView):
    model = models.WorkOrderLaborTask
    serializer_class = serializers.WorkOrderLaborTaskSerializer

    def get_queryset(self):
        queryset = super(WorkOrderWorkOrderLaborTasksList, self).get_queryset()
        return queryset.filter(work_order__work_order_id=self.kwargs.get('work_order_id'))

class WorkOrderWorkOrderMaterialsList(generics.ListAPIView):
    model = models.WorkOrderMaterial
    serializer_class = serializers.WorkOrderMaterialSerializer

    def get_queryset(self):
        queryset = super(WorkOrderWorkOrderMaterialsList, self).get_queryset()
        return queryset.filter(work_order__work_order_id=self.kwargs.get('work_order_id'))

class WorkOrderWorkOrderUnitsList(generics.ListAPIView):
    model = models.WorkOrderUnit
    serializer_class = serializers.WorkOrderUnitSerializer

    def get_queryset(self):
        queryset = super(WorkOrderWorkOrderUnitsList, self).get_queryset()
        return queryset.filter(work_order__work_order_id=self.kwargs.get('work_order_id'))

class WorkOrderWorkOrderVehiclesList(generics.ListAPIView):
    model = models.WorkOrderVehicle
    serializer_class = serializers.WorkOrderVehicleSerializer

    def get_queryset(self):
        queryset = super(WorkOrderWorkOrderVehiclesList, self).get_queryset()
        return queryset.filter(work_order__work_order_id=self.kwargs.get('work_order_id'))

class WorkOrderCommentList(generics.ListCreateAPIView):
    model = models.WorkOrderComment
    serializer_class = serializers.WorkOrderCommentSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.WorkOrderComment
    lookup_field = 'work_order_comment_id'
    serializer_class = serializers.WorkOrderCommentSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class EquipmentItemList(generics.ListCreateAPIView):
    model = models.EquipmentItem
    serializer_class = serializers.EquipmentItemSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class EquipmentItemDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.EquipmentItem
    lookup_field = 'equipment_item_id'
    serializer_class = serializers.EquipmentItemSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class InstallationServiceList(generics.ListCreateAPIView):
    model = models.InstallationService
    serializer_class = serializers.InstallationServiceSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class InstallationServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.InstallationService
    lookup_field = 'installation_service_id'
    serializer_class = serializers.InstallationServiceSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class LaborCategoryList(generics.ListCreateAPIView):
    model = models.LaborCategory
    serializer_class = serializers.LaborCategorySerializer
    permission_classes = [
        permissions.AllowAny
    ]

class LaborCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.LaborCategory
    lookup_field = 'labor_category_id'
    serializer_class = serializers.LaborCategorySerializer
    permission_classes = [
        permissions.AllowAny
    ]

class LaborTaskList(generics.ListCreateAPIView):
    model = models.LaborTask
    serializer_class = serializers.LaborTaskSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class LaborTaskDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.LaborTask
    lookup_field = 'labor_task_id'
    serializer_class = serializers.LaborTaskSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class MaterialList(generics.ListCreateAPIView):
    model = models.Material
    serializer_class = serializers.MaterialSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class MaterialDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.Material
    lookup_field = 'material_id'
    serializer_class = serializers.MaterialSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class VehicleTypeList(generics.ListCreateAPIView):
    model = models.VehicleType
    serializer_class = serializers.VehicleTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class VehicleTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.VehicleType
    lookup_field = 'vehicle_type_id'
    serializer_class = serializers.VehicleTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class UnitList(generics.ListCreateAPIView):
    model = models.Unit
    serializer_class = serializers.UnitSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class UnitDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.Unit
    lookup_field = 'unit_id'
    serializer_class = serializers.UnitSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderEquipmentItemList(generics.ListCreateAPIView):
    model = models.WorkOrderEquipmentItem
    serializer_class = serializers.WorkOrderEquipmentItemSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderEquipmentItemDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.WorkOrderEquipmentItem
    lookup_field = 'work_order_equipment_item_id'
    serializer_class = serializers.WorkOrderEquipmentItemSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderInstallServiceList(generics.ListCreateAPIView):
    model = models.WorkOrderInstallService
    serializer_class = serializers.WorkOrderInstallServiceSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderInstallServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.WorkOrderInstallService
    lookup_field = 'work_order_install_service_id'
    serializer_class = serializers.WorkOrderInstallServiceSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderLaborTaskList(generics.ListCreateAPIView):
    model = models.WorkOrderLaborTask
    serializer_class = serializers.WorkOrderLaborTaskSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderLaborTaskDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.WorkOrderLaborTask
    lookup_field = 'work_order_labor_task_id'
    serializer_class = serializers.WorkOrderLaborTaskSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderMaterialList(generics.ListCreateAPIView):
    model = models.WorkOrderMaterial
    serializer_class = serializers.WorkOrderMaterialSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderMaterialDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.WorkOrderMaterial
    lookup_field = 'work_order_material_id'
    serializer_class = serializers.WorkOrderMaterialSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderUnitList(generics.ListCreateAPIView):
    model = models.WorkOrderUnit
    serializer_class = serializers.WorkOrderUnitSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderUnitDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.WorkOrderUnit
    lookup_field = 'work_order_unit_id'
    serializer_class = serializers.WorkOrderUnitSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderVehicleList(generics.ListCreateAPIView):
    model = models.WorkOrderVehicle
    serializer_class = serializers.WorkOrderVehicleSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderVehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    model = models.WorkOrderVehicle
    lookup_field = 'work_order_vehicle_id'
    serializer_class = serializers.WorkOrderVehicleSerializer
    permission_classes = [
        permissions.AllowAny
    ]

