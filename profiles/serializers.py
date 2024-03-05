from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    email = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        model=Profile
        fields=[
        'id', 'owner', 'created_at', 'updated_at', 'name', 'bio',
        'home_country', 'gender', 'birthdate', 'image', 'email'
        ]