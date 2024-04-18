from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model, handling serialization of user profiles
    along with custom logic for dynamically computed fields like ownership
    status and following relationships.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    email = serializers.ReadOnlyField(source='owner.email')
    paintings_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Determine if the current request user is the owner of the profile.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        """
        Retrieves the ID of the Follower instance if the current user is
        following the owner of the profile, else returns None.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(owner=user,
                                                followed=obj.owner
                                                ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name', 'bio',
            'home_country', 'gender', 'birthdate', 'image', 'email',
            'is_owner', 'following_id', 'paintings_count', 'followers_count',
            'following_count',
        ]
