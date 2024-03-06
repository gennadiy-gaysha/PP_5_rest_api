from rest_framework import serializers
from .models import Observation
from django.db import IntegrityError


class ObservationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Observation model
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Observation
        fields = ['id', 'created_at', 'owner', 'painting']

    def create(self, validated_data):
        '''
        The create function in ObservationSerializer class is an overridden
        method from Django's ModelSerializer class, which is used to handle
        the creation of new instances of the Observation model based on the
        validated data received from an API request.
        '''
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
