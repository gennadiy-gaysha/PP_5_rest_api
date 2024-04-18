from rest_framework import serializers
from .models import Observation
from django.db import IntegrityError


class ObservationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Observation model, which represents observations made by
    users. This serializer handles the serialization of the Observation
    instances and includes custom logic in the creation process to manage
    data integrity and prevent duplicate entries.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """
        Metadata class that defines the model and fields to be serialized.
        It specifies that the Observation model's id, creation time, owner, and
        associated painting are included in the serialized output.
        """
        model = Observation
        fields = ['id', 'created_at', 'owner', 'painting']

    def create(self, validated_data):
        """
        The create function in ObservationSerializer class is an overridden
        method from Django's ModelSerializer class, which is used to handle
        the creation of new instances of the Observation model based on the
        validated data received from an API request.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
