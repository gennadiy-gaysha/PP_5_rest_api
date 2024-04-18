from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Follower model that includes both serialization of
    follower relationships and custom creation logic to handle potential
    integrity errors such as duplicate follower relationships.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = ['id', 'owner', 'created_at', 'followed', 'followed_name']

    def create(self, validated_data):
        """
        The create function in FollowerSerializer class is an overridden
        method from Django's ModelSerializer class, which is used to handle
        the creation of new instances of the Follower model based on the
        validated data received from an API request.

        Args:
            validated_data (dict): Data validated by the serializer to be used
                                   to create a new Follower instance.

        Returns:
            Follower: The newly created Follower instance.

        Raises:
            serializers.ValidationError: If an IntegrityError occurs,
            indicating a duplicate entry.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate',
            })
