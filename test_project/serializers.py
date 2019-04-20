from rest_framework import serializers
# from .models import Participant
from .models import Measurement
from django.contrib.auth.models import User


class ParticipantSerializer(serializers.ModelSerializer):
    # active = serializers.
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'