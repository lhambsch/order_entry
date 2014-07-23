from rest_framework import generics, permissions

from .serializers import CustomerTypeSerializer, CustomerSerializer, CompetitorSerializer, CustomerAddressSerializer
from .models import CustomerType, Customer, Competitor, CustomerAddress


class CustomerTypeList(generics.ListCreateAPIView):
    model = CustomerType
    serializer_class = CustomerTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class CustomerTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = CustomerType
    lookup_field = 'customer_type_id'
    serializer_class = CustomerTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class CompetitorList(generics.ListCreateAPIView):
    model = Competitor
    serializer_class = CompetitorSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class CompetitorDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Competitor
    lookup_field = 'competitor_id'
    serializer_class = CompetitorSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class CustomerList(generics.ListCreateAPIView):
    model = Customer
    serializer_class = CustomerSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Customer
    lookup_field = 'customer_id'
    serializer_class = CustomerSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class CustomerContactList(generics.ListAPIView):
    model = Contact
    serializer_class = ContactSerializer

    def get_queryset(self):
        queryset = super(CustomerContactList, self).get_queryset()
        return queryset.filter(customer__customer_id=self.kwargs.get('customer_id'))

class CustomerAddressList(generics.ListCreateAPIView):
    model = CustomerAddress
    serializer_class = CustomerAddressSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class CustomerAddressDetail(generics.RetrieveUpdateDestroyAPIView):
    model = CustomerAddress
    lookup_field = 'customer_address_id'
    serializer_class = CustomerAddressSerializer
    permission_classes = [
        permissions.AllowAny
    ]
