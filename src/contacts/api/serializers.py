from rest_framework import serializers
from ..models import ContactTitle, Contact


class ContactTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactTitle

class ContactSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    status = StatusSerializer(required=False)
    contact_title = ContactTitleSerializer()

    class Meta:
        model = Contact
