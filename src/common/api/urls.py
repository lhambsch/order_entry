from django.conf.urls import patterns, url

from .views import (StatusDetail, StatusList, OvertimeTypeDetail, OvertimeTypeList, DriveTimeCodeDetail,
    DriveTimeCodeList, ValuationTypeDetail, ValuationTypeList, PaymentTypeDetail, PaymentTypeList,
    OvertimeCodeDetail, OvertimeCodeList, VehicleTypeDetail, VehicleTypeList, LocationDetail, LocationCustomerList,
    LocationEstimateList, LocationList, ContractorDetail, ContractorList, EffectiveRateDetail, EffectiveRateList,
    RateScheduleDetail, RateScheduleList)


status_urls = patterns('',
    url(r'^/(?P<status_id>[0-9a-zA-Z_-]+)$', StatusDetail.as_view(), name='status_detail'),
    url(r'^$', StatusList.as_view(), name='status_list'),
)

overtime_type_urls = patterns('',
    url(r'^/(?P<overtime_type_id>[0-9a-zA-Z_-]+)$', OvertimeTypeDetail.as_view(), name='overtime_type_detail'),
    url(r'^$', OvertimeTypeList.as_view(), name='overtime_type_list'),
)

drive_time_code_urls = patterns('',
    url(r'^/(?P<drive_time_code_id>[0-9a-zA-Z_-]+)$', DriveTimeCodeDetail.as_view(), name='drive_time_code_detail'),
    url(r'^$', DriveTimeCodeList.as_view(), name='drive_time_code_list'),
)

valuation_type_urls = patterns('',
    url(r'^/(?P<valuation_type_id>[0-9a-zA-Z_-]+)$', ValuationTypeDetail.as_view(), name='valuation_type_detail'),
    url(r'^$', ValuationTypeList.as_view(), name='valuation_type_list'),
)

payment_type_urls = patterns('',
    url(r'^/(?P<payment_type_id>[0-9a-zA-Z_-]+)$', PaymentTypeDetail.as_view(), name='payment_type_detail'),
    url(r'^$', PaymentTypeList.as_view(), name='payment_type_list'),
)

vehicle_type_urls = patterns('',
    url(r'^/(?P<vehicle_type_id>[0-9a-zA-Z_-]+)$', VehicleTypeDetail.as_view(), name='vehicle_type_detail'),
    url(r'^$', VehicleTypeList.as_view(), name='vehicle_type_list'),
)

overtime_code_urls = patterns('',
    url(r'^/(?P<overtime_code_id>[0-9a-zA-Z_-]+)$', OvertimeCodeDetail.as_view(), name='overtime_code_detail'),
    url(r'^$', OvertimeCodeList.as_view(), name='overtime_code_list'),
)

location_urls = patterns('',
    url(r'^/(?P<location_id>[0-9a-zA-Z_-]+)$', LocationDetail.as_view(), name='location_detail'),
    url(r'^/(?P<location_id>[0-9a-zA-Z_-]+)/customers$', LocationCustomerList.as_view(), name='location_customer_list'),
    url(r'^/(?P<location_id>[0-9a-zA-Z_-]+)/estimates$', LocationEstimateList.as_view(), name='location_estimate_list'),
    url(r'^$', LocationList.as_view(), name='location_list'),
)

contractor_urls = patterns('',
    url(r'^/(?P<contractor_id>[0-9a-zA-Z_-]+)$', ContractorDetail.as_view(), name='contractor_detail'),
    url(r'^$', ContractorList.as_view(), name='contractor_list'),
)

effective_rate_urls = patterns('',
    url(r'^/(?P<effective_rate_id>[0-9a-zA-Z_-]+)$', EffectiveRateDetail.as_view(), name='effective_rate_detail'),
    url(r'^$', EffectiveRateList.as_view(), name='effective_rate_list'),
)

rate_schedule_urls = patterns('',
    url(r'^/(?P<rate_schedule_id>[0-9a-zA-Z_-]+)$', RateScheduleDetail.as_view(), name='rate_schedule_detail'),
    url(r'^$', RateScheduleList.as_view(), name='rate_schedule_list'),
)
