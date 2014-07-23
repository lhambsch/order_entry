from rest_framework import generics, permissions

from .serializers import (StatusSerializer, OvertimeTypeSerializer, DriveTimeCodeSerializer, ValuationTypeSerializer,
    PaymentTypeSerializer, VehicleTypeSerializer, OvertimeCodeSerializer, LocationSerializer, ContractorSerializer,
    EffectiveRateSerializer, RateScheduleSerializer)

from .models import (Status, OvertimeType, DriveTimeCode, ValuationType, PaymentType, OvertimeCode, Location,
    Contractor, EffectiveRate, RateSchedule)

class StatusList(generics.ListCreateAPIView):
    model = Status
    serializer_class = StatusSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Status
    lookup_field = 'status_id'
    serializer_class = StatusSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class OvertimeTypeList(generics.ListCreateAPIView):
    model = OvertimeType
    serializer_class = OvertimeTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class OvertimeTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = OvertimeType
    lookup_field = 'overtime_type_id'
    serializer_class = OvertimeTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class DriveTimeCodeList(generics.ListCreateAPIView):
    model = DriveTimeCode
    serializer_class = DriveTimeCodeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class DriveTimeCodeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = DriveTimeCode
    lookup_field = 'drive_time_code_id'
    serializer_class = DriveTimeCodeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class ValuationTypeList(generics.ListCreateAPIView):
    model = ValuationType
    serializer_class = ValuationTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class ValuationTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = ValuationType
    lookup_field = 'valuation_type_id'
    serializer_class = ValuationTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class PaymentTypeList(generics.ListCreateAPIView):
    model = PaymentType
    serializer_class = PaymentTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class PaymentTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = PaymentType
    lookup_field = 'payment_type_id'
    serializer_class = PaymentTypeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class OvertimeCodeList(generics.ListCreateAPIView):
    model = OvertimeCode
    serializer_class = OvertimeCodeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class OvertimeCodeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = OvertimeCode
    lookup_field = 'overtime_code_id'
    serializer_class = OvertimeCodeSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class LocationList(generics.ListCreateAPIView):
    model = Location
    serializer_class = LocationSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Location
    lookup_field = 'location_id'
    serializer_class = LocationSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class LocationCustomerList(generics.ListAPIView):
    model = Customer
    serializer_class = CustomerSerializer

    def get_queryset(self):
        queryset = super(LocationCustomerList, self).get_queryset()
        return queryset.filter(location__location_id=self.kwargs.get('location_id'))

class LocationEstimateList(generics.ListAPIView):
    model = Estimate
    serializer_class = EstimateSerializer

    def get_queryset(self):
        queryset = super(LocationEstimateList, self).get_queryset()
        return queryset.filter(booking_branch__location_id=self.kwargs.get('location_id'))

class EffectiveRateList(generics.ListCreateAPIView):
    model = EffectiveRate
    serializer_class = EffectiveRateSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class EffectiveRateDetail(generics.RetrieveUpdateDestroyAPIView):
    model = EffectiveRate
    lookup_field = 'effective_rate_id'
    serializer_class = EffectiveRateSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class RateScheduleList(generics.ListCreateAPIView):
    model = RateSchedule
    serializer_class = RateScheduleSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class RateScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    model = RateSchedule
    lookup_field = 'rate_schedule_id'
    serializer_class = RateScheduleSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class ContractorList(generics.ListCreateAPIView):
    model = Contractor
    serializer_class = ContractorSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class ContractorDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Contractor
    lookup_field = 'contractor_id'
    serializer_class = ContractorSerializer
    permission_classes = [
        permissions.AllowAny
    ]
