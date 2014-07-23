from django.conf.urls import patterns, url

from .views import (EstimateTypeDetail, EstimateTypeList, ProposalTypeDetail, ProposalTypeList, PricingTypeDetail,
        PricingTypeList, AdditionalChargeTypeDetail, AdditionalChargeTypeList, PrevailingWageDetail, PrevailingWageList)

estimate_urls = patterns('',
    url(r'^/(?P<estimate_id>[0-9a-zA-Z_-]+)$', EstimateDetail.as_view(), name='estimate_detail'),
    url(r'^/(?P<estimate_id>[0-9a-zA-Z_-]+)/work_orders$', EstimateWorkOrderList.as_view(), name='estimate_workorder_list'),
    url(r'^$', EstimateList.as_view(), name='estimate_list'),
)

estimate_type_urls = patterns('',
    url(r'^/(?P<estimate_type_id>[0-9a-zA-Z_-]+)$', EstimateTypeDetail.as_view(), name='estimate_type_detail'),
    url(r'^$', EstimateTypeList.as_view(), name='estimate_type_list'),
)

proposal_type_urls = patterns('',
    url(r'^/(?P<proposal_type_id>[0-9a-zA-Z_-]+)$', ProposalTypeDetail.as_view(), name='proposal_type_detail'),
    url(r'^$', ProposalTypeList.as_view(), name='proposal_type_list'),
)

pricing_type_urls = patterns('',
    url(r'^/(?P<pricing_type_id>[0-9a-zA-Z_-]+)$', PricingTypeDetail.as_view(), name='pricing_type_detail'),
    url(r'^$', PricingTypeList.as_view(), name='pricing_type_list'),
)

additional_charge_type_urls = patterns('',
    url(r'^/(?P<additional_charge_type_id>[0-9a-zA-Z_-]+)$', AdditionalChargeTypeDetail.as_view(), name='additional_charge_type_detail'),
    url(r'^$', AdditionalChargeTypeList.as_view(), name='additional_charge_type_list'),
)

prevailing_wage_urls = patterns('',
    url(r'^/(?P<prevailing_wage_id>[0-9a-zA-Z_-]+)$', PrevailingWageDetail.as_view(), name='prevailing_wage_detail'),
    url(r'^$', PrevailingWageList.as_view(), name='prevailing_wage_list'),
)
