from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """
    Serializer for the current user that extends UserDetailsSerializer from
    dj-rest-auth. This serializer adds profile-specific fields to the user
    details, enabling clients to access the user's profile ID and profile
    image URL alongside standard user information such as username
    and email.

    The added fields are read-only and sourced from the user's associated
    profile model, ensuring that the serializer accurately reflects the
    current state of the user's profile without allowing direct modification
    through this serializer.
    """
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )
