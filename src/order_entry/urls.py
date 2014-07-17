from django.conf.urls import patterns, include, url

from estimates.api import api_views
from estimates.views import HomeView

from django.contrib import admin
admin.autodiscover()

status_urls = patterns('',
    url(r'^/(?P<status_id>[0-9a-zA-Z_-]+)$', api_views.StatusDetail.as_view(), name='status_detail'),
    url(r'^$', api_views.StatusList.as_view(), name='status_list'),
)

customer_type_urls = patterns('',
    url(r'^/(?P<customer_type_id>[0-9a-zA-Z_-]+)$', api_views.CustomerTypeDetail.as_view(), name='customer_type_detail'),
    url(r'^$', api_views.CustomerTypeList.as_view(), name='customer_type_list'),
)

overtime_type_urls = patterns('',
    url(r'^/(?P<overtime_type_id>[0-9a-zA-Z_-]+)$', api_views.OvertimeTypeDetail.as_view(), name='overtime_type_detail'),
    url(r'^$', api_views.OvertimeTypeList.as_view(), name='overtime_type_list'),
)

drive_time_code_urls = patterns('',
    url(r'^/(?P<drive_time_code_id>[0-9a-zA-Z_-]+)$', api_views.DriveTimeCodeDetail.as_view(), name='drive_time_code_detail'),
    url(r'^$', api_views.DriveTimeCodeList.as_view(), name='drive_time_code_list'),
)

valuation_type_urls = patterns('',
    url(r'^/(?P<valuation_type_id>[0-9a-zA-Z_-]+)$', api_views.ValuationTypeDetail.as_view(), name='valuation_type_detail'),
    url(r'^$', api_views.ValuationTypeList.as_view(), name='valuation_type_list'),
)

payment_type_urls = patterns('',
    url(r'^/(?P<payment_type_id>[0-9a-zA-Z_-]+)$', api_views.PaymentTypeDetail.as_view(), name='payment_type_detail'),
    url(r'^$', api_views.PaymentTypeList.as_view(), name='payment_type_list'),
)

competitor_urls = patterns('',
    url(r'^/(?P<competitor_id>[0-9a-zA-Z_-]+)$', api_views.CompetitorDetail.as_view(), name='competitor_detail'),
    url(r'^$', api_views.CompetitorList.as_view(), name='competitor_list'),
)

overtime_code_urls = patterns('',
    url(r'^/(?P<overtime_code_id>[0-9a-zA-Z_-]+)$', api_views.OvertimeCodeDetail.as_view(), name='overtime_code_detail'),
    url(r'^$', api_views.OvertimeCodeList.as_view(), name='overtime_code_list'),
)

location_urls = patterns('',
    url(r'^/(?P<location_id>[0-9a-zA-Z_-]+)$', api_views.LocationDetail.as_view(), name='location_detail'),
    url(r'^/(?P<location_id>[0-9a-zA-Z_-]+)/customers$', api_views.LocationCustomerList.as_view(), name='location_customer_list'),
    url(r'^/(?P<location_id>[0-9a-zA-Z_-]+)/estimates$', api_views.LocationEstimateList.as_view(), name='location_estimate_list'),
    url(r'^$', api_views.LocationList.as_view(), name='location_list'),
)

effective_rate_urls = patterns('',
    url(r'^/(?P<effective_rate_id>[0-9a-zA-Z_-]+)$', api_views.EffectiveRateDetail.as_view(), name='effective_rate_detail'),
    url(r'^$', api_views.EffectiveRateList.as_view(), name='effective_rate_list'),
)

rate_schedule_urls = patterns('',
    url(r'^/(?P<rate_schedule_id>[0-9a-zA-Z_-]+)$', api_views.RateScheduleDetail.as_view(), name='rate_schedule_detail'),
    url(r'^$', api_views.RateScheduleList.as_view(), name='rate_schedule_list'),
)

customer_urls = patterns('',
    url(r'^/(?P<customer_id>[0-9a-zA-Z_-]+)$', api_views.CustomerDetail.as_view(), name='customer_detail'),
    url(r'^/(?P<customer_id>[0-9a-zA-Z_-]+)/contacts$', api_views.CustomerContactList.as_view(), name='customer_contact_list'),
    url(r'^$', api_views.CustomerList.as_view(), name='customer_list'),
)

contact_title_urls = patterns('',
    url(r'^/(?P<contact_title_id>[0-9a-zA-Z_-]+)$', api_views.ContactTitleDetail.as_view(), name='contact_title_detail'),
    url(r'^$', api_views.ContactTitleList.as_view(), name='contact_title_list'),
)

contact_urls = patterns('',
    url(r'^/(?P<contact_id>[0-9a-zA-Z_-]+)$', api_views.ContactDetail.as_view(), name='contact_detail'),
    url(r'^$', api_views.ContactList.as_view(), name='contact_list'),
)

estimate_type_urls = patterns('',
    url(r'^/(?P<estimate_type_id>[0-9a-zA-Z_-]+)$', api_views.EstimateTypeDetail.as_view(), name='estimate_type_detail'),
    url(r'^$', api_views.EstimateTypeList.as_view(), name='estimate_type_list'),
)

proposal_type_urls = patterns('',
    url(r'^/(?P<proposal_type_id>[0-9a-zA-Z_-]+)$', api_views.ProposalTypeDetail.as_view(), name='proposal_type_detail'),
    url(r'^$', api_views.ProposalTypeList.as_view(), name='proposal_type_list'),
)

pricing_type_urls = patterns('',
    url(r'^/(?P<pricing_type_id>[0-9a-zA-Z_-]+)$', api_views.PricingTypeDetail.as_view(), name='pricing_type_detail'),
    url(r'^$', api_views.PricingTypeList.as_view(), name='pricing_type_list'),
)

additional_charge_type_urls = patterns('',
    url(r'^/(?P<additional_charge_type_id>[0-9a-zA-Z_-]+)$', api_views.AdditionalChargeTypeDetail.as_view(), name='additional_charge_type_detail'),
    url(r'^$', api_views.AdditionalChargeTypeList.as_view(), name='additional_charge_type_list'),
)

prevailing_wage_urls = patterns('',
    url(r'^/(?P<prevailing_wage_id>[0-9a-zA-Z_-]+)$', api_views.PrevailingWageDetail.as_view(), name='prevailing_wage_detail'),
    url(r'^$', api_views.PrevailingWageList.as_view(), name='prevailing_wage_list'),
)

contractor_urls = patterns('',
    url(r'^/(?P<contractor_id>[0-9a-zA-Z_-]+)$', api_views.ContractorDetail.as_view(), name='contractor_detail'),
    url(r'^$', api_views.ContractorList.as_view(), name='contractor_list'),
)

estimate_urls = patterns('',
    url(r'^/(?P<estimate_id>[0-9a-zA-Z_-]+)$', api_views.EstimateDetail.as_view(), name='estimate_detail'),
    url(r'^/(?P<estimate_id>[0-9a-zA-Z_-]+)/work_orders$', api_views.EstimateWorkOrderList.as_view(), name='estimate_workorder_list'),
    url(r'^$', api_views.EstimateList.as_view(), name='estimate_list'),
)

work_order_group_urls = patterns('',
    url(r'^/(?P<work_order_group_id>[0-9a-zA-Z_-]+)$', api_views.WorkOrderGroupDetail.as_view(), name='work_order_group_detail'),
    url(r'^$', api_views.WorkOrderGroupList.as_view(), name='work_order_group_list'),
)

customer_address_urls = patterns('',
    url(r'^/(?P<customer_address_id>[0-9a-zA-Z_-]+)$', api_views.CustomerAddressDetail.as_view(), name='customer_address_detail'),
    url(r'^$', api_views.CustomerAddressList.as_view(), name='customer_address_list'),
)

service_line_urls = patterns('',
    url(r'^/(?P<service_line_id>[0-9a-zA-Z_-]+)$', api_views.ServiceLineDetail.as_view(), name='service_line_detail'),
    url(r'^$', api_views.ServiceLineList.as_view(), name='service_line_list'),
)

work_order_urls = patterns('',
    url(r'^/(?P<work_order_id>[0-9a-zA-Z_-]+)$', api_views.WorkOrderDetail.as_view(), name='work_order_detail'),
    url(r'^/(?P<work_order_id>[0-9a-zA-Z_-]+)/work_order_comments$', api_views.WorkOrderWorkOrderCommentsList.as_view(), name='workorder_workordercomments_list'),
    url(r'^/(?P<work_order_id>[0-9a-zA-Z_-]+)/work_order_equipment_items$', api_views.WorkOrderWorkOrderEquipmentItemsList.as_view(), name='workorder_workorderequipmentitems_list'),
    url(r'^/(?P<work_order_id>[0-9a-zA-Z_-]+)/work_order_install_services$', api_views.WorkOrderWorkOrderInstallServicesList.as_view(), name='workorder_workorderinstallservices_list'),
    url(r'^/(?P<work_order_id>[0-9a-zA-Z_-]+)/work_order_labor_tasks$', api_views.WorkOrderWorkOrderLaborTasksList.as_view(), name='workorder_workorderlabortasks_list'),
    url(r'^/(?P<work_order_id>[0-9a-zA-Z_-]+)/work_order_materials$', api_views.WorkOrderWorkOrderMaterialsList.as_view(), name='workorder_workordermaterials_list'),
    url(r'^/(?P<work_order_id>[0-9a-zA-Z_-]+)/work_order_units$', api_views.WorkOrderWorkOrderUnitsList.as_view(), name='workorder_workorderunits_list'),
    url(r'^/(?P<work_order_id>[0-9a-zA-Z_-]+)/work_order_vehicles$', api_views.WorkOrderWorkOrderVehiclesList.as_view(), name='workorder_workordervehicles_list'),
    url(r'^$', api_views.WorkOrderList.as_view(), name='work_order_list'),
)

equipment_item_urls = patterns('',
    url(r'^/(?P<equipment_item_id>[0-9a-zA-Z_-]+)$', api_views.EquipmentItemDetail.as_view(), name='equipment_item_detail'),
    url(r'^$', api_views.EquipmentItemList.as_view(), name='equipment_item_list'),
)

installation_service_urls = patterns('',
    url(r'^/(?P<installation_service_id>[0-9a-zA-Z_-]+)$', api_views.InstallationServiceDetail.as_view(), name='installation_service_detail'),
    url(r'^$', api_views.InstallationServiceList.as_view(), name='installation_service_list'),
)

labor_category_urls = patterns('',
    url(r'^/(?P<labor_category_id>[0-9a-zA-Z_-]+)$', api_views.LaborCategoryDetail.as_view(), name='labor_category_detail'),
    url(r'^$', api_views.LaborCategoryList.as_view(), name='labor_category_list'),
)

labor_task_urls = patterns('',
    url(r'^/(?P<labor_task_id>[0-9a-zA-Z_-]+)$', api_views.LaborTaskDetail.as_view(), name='labor_task_detail'),
    url(r'^$', api_views.LaborTaskList.as_view(), name='labor_task_list'),
)

material_urls = patterns('',
    url(r'^/(?P<material_id>[0-9a-zA-Z_-]+)$', api_views.MaterialDetail.as_view(), name='material_detail'),
    url(r'^$', api_views.MaterialList.as_view(), name='material_list'),
)

vehicle_type_urls = patterns('',
    url(r'^/(?P<vehicle_type_id>[0-9a-zA-Z_-]+)$', api_views.VehicleTypeDetail.as_view(), name='vehicle_type_detail'),
    url(r'^$', api_views.VehicleTypeList.as_view(), name='vehicle_type_list'),
)

unit_urls = patterns('',
    url(r'^/(?P<unit_id>[0-9a-zA-Z_-]+)$', api_views.UnitDetail.as_view(), name='unit_detail'),
    url(r'^$', api_views.UnitList.as_view(), name='unit_list'),
)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'order_entry.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^statuses', include(status_urls)),
    url(r'^customer_types', include(customer_type_urls)),
    url(r'^overtime_types', include(overtime_type_urls)),
    url(r'^drive_time_codes', include(drive_time_code_urls)),
    url(r'^valuation_types', include(valuation_type_urls)),
    url(r'^payment_types', include(payment_type_urls)),
    url(r'^competitors', include(competitor_urls)),
    url(r'^overtime_codes', include(overtime_code_urls)),
    url(r'^locations', include(location_urls)),
    url(r'^effective_rates', include(effective_rate_urls)),
    url(r'^rate_schedules', include(rate_schedule_urls)),
    url(r'^customers', include(customer_urls)),
    url(r'^contact_titles', include(contact_title_urls)),
    url(r'^contacts', include(contact_urls)),
    url(r'^estimate_types', include(estimate_type_urls)),
    url(r'^proposal_types', include(proposal_type_urls)),
    url(r'^pricing_types', include(pricing_type_urls)),
    url(r'^additional_charge_types', include(additional_charge_type_urls)),
    url(r'^prevailing_wages', include(prevailing_wage_urls)),
    url(r'^contractors', include(contractor_urls)),
    url(r'^estimates', include(estimate_urls)),
    url(r'^work_order_groups', include(work_order_group_urls)),
    url(r'^customer_addresses', include(customer_address_urls)),
    url(r'^service_lines', include(service_line_urls)),
    url(r'^work_orders', include(work_order_urls)),
    url(r'^equipment_items', include(equipment_item_urls)),
    url(r'^installation_services', include(installation_service_urls)),
    url(r'^labor_categories', include(labor_category_urls)),
    url(r'^labor_tasks', include(labor_task_urls)),
    url(r'^materials', include(material_urls)),
    url(r'^vehicle_types', include(vehicle_type_urls)),
    url(r'^units', include(unit_urls)),
)
