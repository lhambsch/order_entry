from rest_framework import generics, permissions

from .serializers import (EstimateTypeSerializer, EstimateSerializer, ProposalTypeSerializer, PricingTypeSerializer,
    AdditionalChargeTypeSerializer, PrevailingWageSerializer)

from ..models import EstimateType, Estimate, ProposalType, PricingType, AdditionalChargeType, PrevailingWage


class EstimateTypeList(generics.ListCreateAPIView):
    model = EstimateType
    serializer_class = EstimateTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class EstimateTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = EstimateType
    lookup_field = 'estimate_type_id'
    serializer_class = EstimateTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class ProposalTypeList(generics.ListCreateAPIView):
    model = ProposalType
    serializer_class = ProposalTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class ProposalTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = ProposalType
    lookup_field = 'proposal_type_id'
    serializer_class = ProposalTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class PricingTypeList(generics.ListCreateAPIView):
    model = PricingType
    serializer_class = PricingTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class PricingTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = PricingType
    lookup_field = 'pricing_type_id'
    serializer_class = PricingTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class AdditionalChargeTypeList(generics.ListCreateAPIView):
    model = AdditionalChargeType
    serializer_class = AdditionalChargeTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class AdditionalChargeTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = AdditionalChargeType
    lookup_field = 'additional_charge_type_id'
    serializer_class = AdditionalChargeTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class PrevailingWageList(generics.ListCreateAPIView):
    model = PrevailingWage
    serializer_class = PrevailingWageSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class PrevailingWageDetail(generics.RetrieveUpdateDestroyAPIView):
    model = PrevailingWage
    lookup_field = 'prevailing_wage_id'
    serializer_class = PrevailingWageSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class EstimateList(generics.ListCreateAPIView):
    model = Estimate
    serializer_class = EstimateSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class EstimateDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Estimate
    lookup_field = 'estimate_id'
    serializer_class = EstimateSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class EstimateWorkOrderList(generics.ListAPIView):
    model = WorkOrder
    serializer_class = WorkOrderSerializer

    def get_queryset(self):
        queryset = super(EstimateWorkOrderList, self).get_queryset()
        return queryset.filter(estimate__estimate_id=self.kwargs.get('estimate_id'))
