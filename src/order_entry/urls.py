from django.conf.urls import patterns, include, url

from estimates.api.urls import (estimate_urls, estimate_type_urls, proposal_type_urls, pricing_type_urls,
    additional_charge_type_urls, prevailing_wage_urls)

from common.api.urls import (status_urls, overtime_type_urls, drive_time_code_urls, valuation_type_urls,
    payment_type_urls, vehicle_type_urls, overtime_code_urls, location_urls, contractor_urls, effective_rate_urls,
    rate_schedule_urls)

from customers.api.urls import customer_type_urls, customer_urls, competitor_urls, customer_address_urls
from contacts.api.urls import contact_title_urls, contact_urls

from work_orders.urls import (work_order_group_urls, service_line_urls, work_order_urls, equipment_item_urls,
    installation_service_urls, labor_category_urls, labor_task_urls, material_urls, unit_urls)

from common.views import HomeView

from django.contrib import admin
admin.autodiscover()


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
