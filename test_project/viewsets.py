from rest_framework import viewsets
from .models import Participant, Measurement
from django.contrib.auth.models import User
from .serializers import ParticipantSerializer, MeasurementSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class EmployeeViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    queryset = User.objects.all().order_by("id")
    serializer_class = ParticipantSerializer
    #
    # def list(self, request, *args, **kwargs):
    #
    #     return Response('test1') if any([args, kwargs]) else Response({'say': 'test2'})


class MeasurementViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Measurement.objects.all().order_by("id")
    serializer_class = MeasurementSerializer
