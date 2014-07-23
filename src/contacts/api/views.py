from rest_framework import generics, permissions

from .serializers import ContactTitleSerializer, ContactSerializer
from ..models import ContactTitle, Contact


class ContactTitleList(generics.ListCreateAPIView):
    model = ContactTitle
    serializer_class = ContactTitleSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class ContactTitleDetail(generics.RetrieveUpdateDestroyAPIView):
    model = ContactTitle
    lookup_field = 'contact_title_id'
    serializer_class = ContactTitleSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class ContactList(generics.ListCreateAPIView):
    model = Contact
    serializer_class = ContactSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Contact
    lookup_field = 'contact_id'
    serializer_class = ContactSerializer
    permission_classes = [
        permissions.AllowAny
    ]
