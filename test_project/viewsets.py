from rest_framework import viewsets
from .models import Participant
from .serializers import ParticipantSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class EmployeeViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    queryset = Participant.objects.all().order_by("id")
    serializer_class = ParticipantSerializer
    #
    # def list(self, request, *args, **kwargs):
    #
    #     return Response('yala-yala') if any([args, kwargs]) else Response({'say': 'ку-ку, ёпт!'})
