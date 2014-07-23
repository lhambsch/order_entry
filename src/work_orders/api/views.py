from rest_framework import generics, permissions

from .serializers import (WorkOrderGroupSerializer, ServiceLineSerializer, WorkOrderSerializer, EquipmentItemSerializer,
    InstallationServiceSerializer, LaborCategorySerializer, LaborTaskSerializer, MaterialSerializer, UnitSerializer)

from ..models import (WorkOrderGroup, ServiceLine, WorkOrder, EquipmentItem, InstallationService, LaborCategory,
    LaborTask, Material, Unit)


class WorkOrderGroupList(generics.ListCreateAPIView):
    model = WorkOrderGroup
    serializer_class = WorkOrderGroupSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    model = WorkOrderGroup
    lookup_field = 'work_order_group_id'
    serializer_class = WorkOrderGroupSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class ServiceLineList(generics.ListCreateAPIView):
    model = ServiceLine
    serializer_class = ServiceLineSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class ServiceLineDetail(generics.RetrieveUpdateDestroyAPIView):
    model = ServiceLine
    lookup_field = 'service_line_id'
    serializer_class = ServiceLineSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderList(generics.ListCreateAPIView):
    model = WorkOrder
    serializer_class = WorkOrderSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    model = WorkOrder
    lookup_field = 'work_order_id'
    serializer_class = WorkOrderSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderWorkOrderCommentsList(generics.ListAPIView):
    model = WorkOrderComment
    serializer_class = WorkOrderCommentSerializer

    def get_queryset(self):
        queryset = super(WorkOrderWorkOrderCommentsList, self).get_queryset()
        return queryset.filter(work_order__work_order_id=self.kwargs.get('work_order_id'))

class WorkOrderWorkOrderEquipmentItemsList(generics.ListAPIView):
    model = WorkOrderEquipmentItem
    serializer_class = WorkOrderEquipmentItemSerializer

    def get_queryset(self):
        queryset = super(WorkOrderWorkOrderEquipmentItemsList, self).get_queryset()
        return queryset.filter(work_order__work_order_id=self.kwargs.get('work_order_id'))

class WorkOrderWorkOrderInstallServicesList(generics.ListAPIView):
    model = WorkOrderInstallService
    serializer_class = WorkOrderInstallServiceSerializer

    def get_queryset(self):
        queryset = super(WorkOrderWorkOrderInstallServicesList, self).get_queryset()
        return queryset.filter(work_order__work_order_id=self.kwargs.get('work_order_id'))

class WorkOrderWorkOrderLaborTasksList(generics.ListAPIView):
    model = WorkOrderLaborTask
    serializer_class = WorkOrderLaborTaskSerializer

    def get_queryset(self):
        queryset = super(WorkOrderWorkOrderLaborTasksList, self).get_queryset()
        return queryset.filter(work_order__work_order_id=self.kwargs.get('work_order_id'))

class WorkOrderWorkOrderMaterialsList(generics.ListAPIView):
    model = WorkOrderMaterial
    serializer_class = WorkOrderMaterialSerializer

    def get_queryset(self):
        queryset = super(WorkOrderWorkOrderMaterialsList, self).get_queryset()
        return queryset.filter(work_order__work_order_id=self.kwargs.get('work_order_id'))

class WorkOrderWorkOrderUnitsList(generics.ListAPIView):
    model = WorkOrderUnit
    serializer_class = WorkOrderUnitSerializer

    def get_queryset(self):
        queryset = super(WorkOrderWorkOrderUnitsList, self).get_queryset()
        return queryset.filter(work_order__work_order_id=self.kwargs.get('work_order_id'))

class WorkOrderWorkOrderVehiclesList(generics.ListAPIView):
    model = WorkOrderVehicle
    serializer_class = WorkOrderVehicleSerializer

    def get_queryset(self):
        queryset = super(WorkOrderWorkOrderVehiclesList, self).get_queryset()
        return queryset.filter(work_order__work_order_id=self.kwargs.get('work_order_id'))

class WorkOrderCommentList(generics.ListCreateAPIView):
    model = WorkOrderComment
    serializer_class = WorkOrderCommentSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    model = WorkOrderComment
    lookup_field = 'work_order_comment_id'
    serializer_class = WorkOrderCommentSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class EquipmentItemList(generics.ListCreateAPIView):
    model = EquipmentItem
    serializer_class = EquipmentItemSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class EquipmentItemDetail(generics.RetrieveUpdateDestroyAPIView):
    model = EquipmentItem
    lookup_field = 'equipment_item_id'
    serializer_class = EquipmentItemSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class InstallationServiceList(generics.ListCreateAPIView):
    model = InstallationService
    serializer_class = InstallationServiceSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class InstallationServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    model = InstallationService
    lookup_field = 'installation_service_id'
    serializer_class = InstallationServiceSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class LaborCategoryList(generics.ListCreateAPIView):
    model = LaborCategory
    serializer_class = LaborCategorySerializer
    permission_classes = [
        permissions.AllowAny
    ]

class LaborCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    model = LaborCategory
    lookup_field = 'labor_category_id'
    serializer_class = LaborCategorySerializer
    permission_classes = [
        permissions.AllowAny
    ]

class LaborTaskList(generics.ListCreateAPIView):
    model = LaborTask
    serializer_class = LaborTaskSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class LaborTaskDetail(generics.RetrieveUpdateDestroyAPIView):
    model = LaborTask
    lookup_field = 'labor_task_id'
    serializer_class = LaborTaskSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class MaterialList(generics.ListCreateAPIView):
    model = Material
    serializer_class = MaterialSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class MaterialDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Material
    lookup_field = 'material_id'
    serializer_class = MaterialSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class VehicleTypeList(generics.ListCreateAPIView):
    model = VehicleType
    serializer_class = VehicleTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class VehicleTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = VehicleType
    lookup_field = 'vehicle_type_id'
    serializer_class = VehicleTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class UnitList(generics.ListCreateAPIView):
    model = Unit
    serializer_class = UnitSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class UnitDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Unit
    lookup_field = 'unit_id'
    serializer_class = UnitSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderEquipmentItemList(generics.ListCreateAPIView):
    model = WorkOrderEquipmentItem
    serializer_class = WorkOrderEquipmentItemSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderEquipmentItemDetail(generics.RetrieveUpdateDestroyAPIView):
    model = WorkOrderEquipmentItem
    lookup_field = 'work_order_equipment_item_id'
    serializer_class = WorkOrderEquipmentItemSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderInstallServiceList(generics.ListCreateAPIView):
    model = WorkOrderInstallService
    serializer_class = WorkOrderInstallServiceSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderInstallServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    model = WorkOrderInstallService
    lookup_field = 'work_order_install_service_id'
    serializer_class = WorkOrderInstallServiceSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderLaborTaskList(generics.ListCreateAPIView):
    model = WorkOrderLaborTask
    serializer_class = WorkOrderLaborTaskSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderLaborTaskDetail(generics.RetrieveUpdateDestroyAPIView):
    model = WorkOrderLaborTask
    lookup_field = 'work_order_labor_task_id'
    serializer_class = WorkOrderLaborTaskSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderMaterialList(generics.ListCreateAPIView):
    model = WorkOrderMaterial
    serializer_class = WorkOrderMaterialSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderMaterialDetail(generics.RetrieveUpdateDestroyAPIView):
    model = WorkOrderMaterial
    lookup_field = 'work_order_material_id'
    serializer_class = WorkOrderMaterialSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderUnitList(generics.ListCreateAPIView):
    model = WorkOrderUnit
    serializer_class = WorkOrderUnitSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderUnitDetail(generics.RetrieveUpdateDestroyAPIView):
    model = WorkOrderUnit
    lookup_field = 'work_order_unit_id'
    serializer_class = WorkOrderUnitSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderVehicleList(generics.ListCreateAPIView):
    model = WorkOrderVehicle
    serializer_class = WorkOrderVehicleSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class WorkOrderVehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    model = WorkOrderVehicle
    lookup_field = 'work_order_vehicle_id'
    serializer_class = WorkOrderVehicleSerializer
    permission_classes = [
        permissions.AllowAny
    ]
