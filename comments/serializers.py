from rest_framework import serializers
from .models import Comment
from django.contrib.humanize.templatetags.humanize import naturaltime


class CommentSerializer(serializers.ModelSerializer):
    """
    A serializer for the Comment model, providing serialization for basic
    attributes along with custom methods to display whether the request user
    is the owner of the comment and formatted timestamps.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    is_owner = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Determine if the current request user is the owner of the comment.
        This method takes an instance of the object being serialized (obj) as
        its argument. Retrieves the current request object from self.context[
        'request']. The context is a dictionary that serializers have, which
        can carry additional information, including the current request. The
        context must be passed to the serializer at the time of its
        initialization (typically in views).
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        """
        Return a human-readable time since the comment was created.
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Return a human-readable time since the comment was last updated.
        """
        return naturaltime(obj.updated_at)

    class Meta:
        model = Comment
        fields = ['id', 'owner', 'is_owner', 'profile_id', 'profile_image',
                  'painting', 'created_at', 'updated_at', 'content']


class CommentDetailSerializer(CommentSerializer):
    """
    A serializer for displaying detailed information of a Comment,
    extending CommentSerializer with an additional field to display the
    associated painting's ID.
    """
    painting = serializers.ReadOnlyField(source='painting.id')
