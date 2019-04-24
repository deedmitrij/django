from rest_framework import serializers
from .models import Participant, Measurement
from django.contrib.auth.models import User


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'
        exclude_when_nested = ('user_id',)

    def get_field_names(self, *args, **kwargs):
        field_names = super(MeasurementSerializer, self).get_field_names(*args, **kwargs)
        if self.parent:
            field_names = [i for i in field_names if i not in self.Meta.exclude_when_nested]
        return field_names


class ParticipantSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True, read_only=True)
    weight = serializers.SerializerMethodField(method_name='get_user_weight')

    class Meta:
        model = Participant
        fields = ('name', 'email', 'weight', 'measurements', 'active')

    def get_user_weight(self, request):
        return Measurement.objects.filter(user_id=request.id).latest('date').weight
