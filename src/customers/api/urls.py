from django.conf.urls import patterns, url

from .views import (CustomerTypeDetail, CustomerTypeList, CustomerDetail, CustomerContactList, CustomerList,
    CompetitorDetail, CompetitorList, CustomerAddressDetail, CustomerAddressList)


customer_type_urls = patterns('',
    url(r'^/(?P<customer_type_id>[0-9a-zA-Z_-]+)$', CustomerTypeDetail.as_view(), name='customer_type_detail'),
    url(r'^$', CustomerTypeList.as_view(), name='customer_type_list'),
)

customer_urls = patterns('',
    url(r'^/(?P<customer_id>[0-9a-zA-Z_-]+)$', CustomerDetail.as_view(), name='customer_detail'),
    url(r'^/(?P<customer_id>[0-9a-zA-Z_-]+)/contacts$', CustomerContactList.as_view(), name='customer_contact_list'),
    url(r'^$', CustomerList.as_view(), name='customer_list'),
)

competitor_urls = patterns('',
    url(r'^/(?P<competitor_id>[0-9a-zA-Z_-]+)$', CompetitorDetail.as_view(), name='competitor_detail'),
    url(r'^$', CompetitorList.as_view(), name='competitor_list'),
)

customer_address_urls = patterns('',
    url(r'^/(?P<customer_address_id>[0-9a-zA-Z_-]+)$', CustomerAddressDetail.as_view(), name='customer_address_detail'),
    url(r'^$', CustomerAddressList.as_view(), name='customer_address_list'),
)
