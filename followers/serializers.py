from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
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
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate',
            })
