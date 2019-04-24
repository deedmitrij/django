from rest_framework import viewsets
from .models import Participant, Measurement
from django.contrib.auth.models import User
from .serializers import ParticipantSerializer, MeasurementSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Prefetch


class EmployeeViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Participant.objects.prefetch_related(Prefetch('measurements', queryset=Measurement.objects.order_by('-date')))
    serializer_class = ParticipantSerializer


class MeasurementViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Measurement.objects.all().order_by("id")
    serializer_class = MeasurementSerializer
