from django.conf.urls import patterns, url

from .views import (WorkOrderGroupDetail, WorkOrderGroupList, ServiceLineDetail, ServiceLineList,
    WorkOrderDetail, WorkOrderWorkOrderCommentsList, WorkOrderWorkOrderEquipmentItemsList,
    WorkOrderWorkOrderInstallServicesList, WorkOrderWorkOrderLaborTasksList, WorkOrderWorkOrderMaterialsList,
    WorkOrderWorkOrderUnitsList, WorkOrderWorkOrderVehiclesList, WorkOrderList)

work_order_group_urls = patterns('',
    url(r'^/(?P<work_order_group_id>[0-9a-zA-Z_-]+)$', WorkOrderGroupDetail.as_view(), name='work_order_group_detail'),
    url(r'^$', WorkOrderGroupList.as_view(), name='work_order_group_list'),
)

service_line_urls = patterns('',
    url(r'^/(?P<service_line_id>[0-9a-zA-Z_-]+)$', ServiceLineDetail.as_view(), name='service_line_detail'),
    url(r'^$', ServiceLineList.as_view(), name='service_line_list'),
)

work_order_urls = patterns('',
    url(r'^/(?P<work_order_id>[0-9a-zA-Z_-]+)$', WorkOrderDetail.as_view(), name='work_order_detail'),
    url(r'^/(?P<work_order_id>[0-9a-zA-Z_-]+)/work_order_comments$', WorkOrderWorkOrderCommentsList.as_view(), name='workorder_workordercomments_list'),
    url(r'^/(?P<work_order_id>[0-9a-zA-Z_-]+)/work_order_equipment_items$', WorkOrderWorkOrderEquipmentItemsList.as_view(), name='workorder_workorderequipmentitems_list'),
    url(r'^/(?P<work_order_id>[0-9a-zA-Z_-]+)/work_order_install_services$', WorkOrderWorkOrderInstallServicesList.as_view(), name='workorder_workorderinstallservices_list'),
    url(r'^/(?P<work_order_id>[0-9a-zA-Z_-]+)/work_order_labor_tasks$', WorkOrderWorkOrderLaborTasksList.as_view(), name='workorder_workorderlabortasks_list'),
    url(r'^/(?P<work_order_id>[0-9a-zA-Z_-]+)/work_order_materials$', WorkOrderWorkOrderMaterialsList.as_view(), name='workorder_workordermaterials_list'),
    url(r'^/(?P<work_order_id>[0-9a-zA-Z_-]+)/work_order_units$', WorkOrderWorkOrderUnitsList.as_view(), name='workorder_workorderunits_list'),
    url(r'^/(?P<work_order_id>[0-9a-zA-Z_-]+)/work_order_vehicles$', WorkOrderWorkOrderVehiclesList.as_view(), name='workorder_workordervehicles_list'),
    url(r'^$', WorkOrderList.as_view(), name='work_order_list'),
)

equipment_item_urls = patterns('',
    url(r'^/(?P<equipment_item_id>[0-9a-zA-Z_-]+)$', EquipmentItemDetail.as_view(), name='equipment_item_detail'),
    url(r'^$', EquipmentItemList.as_view(), name='equipment_item_list'),
)

installation_service_urls = patterns('',
    url(r'^/(?P<installation_service_id>[0-9a-zA-Z_-]+)$', InstallationServiceDetail.as_view(), name='installation_service_detail'),
    url(r'^$', InstallationServiceList.as_view(), name='installation_service_list'),
)

labor_category_urls = patterns('',
    url(r'^/(?P<labor_category_id>[0-9a-zA-Z_-]+)$', LaborCategoryDetail.as_view(), name='labor_category_detail'),
    url(r'^$', LaborCategoryList.as_view(), name='labor_category_list'),
)

labor_task_urls = patterns('',
    url(r'^/(?P<labor_task_id>[0-9a-zA-Z_-]+)$', LaborTaskDetail.as_view(), name='labor_task_detail'),
    url(r'^$', LaborTaskList.as_view(), name='labor_task_list'),
)

material_urls = patterns('',
    url(r'^/(?P<material_id>[0-9a-zA-Z_-]+)$', MaterialDetail.as_view(), name='material_detail'),
    url(r'^$', MaterialList.as_view(), name='material_list'),
)

unit_urls = patterns('',
    url(r'^/(?P<unit_id>[0-9a-zA-Z_-]+)$', UnitDetail.as_view(), name='unit_detail'),
    url(r'^$', UnitList.as_view(), name='unit_list'),
)
