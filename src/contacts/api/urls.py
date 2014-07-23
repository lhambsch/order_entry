from django.conf.urls import patterns, url

from .views import ContactTitleDetail, ContactTitleList, ContactDetail, ContactList


contact_title_urls = patterns('',
    url(r'^/(?P<contact_title_id>[0-9a-zA-Z_-]+)$', ContactTitleDetail.as_view(), name='contact_title_detail'),
    url(r'^$', ContactTitleList.as_view(), name='contact_title_list'),
)

contact_urls = patterns('',
    url(r'^/(?P<contact_id>[0-9a-zA-Z_-]+)$', ContactDetail.as_view(), name='contact_detail'),
    url(r'^$', ContactList.as_view(), name='contact_list'),
)
