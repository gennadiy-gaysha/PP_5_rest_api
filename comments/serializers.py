from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        '''
        This method takes an instance of the object being serialized (obj) as
        its argument. Retrieves the current request object from self.context[
        'request']. The context is a dictionary that serializers have, which
        can carry additional information, including the current request. The
        context must be passed to the serializer at the time of its
        initialization (typically in views).
        '''
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = ['id', 'owner', 'is_owner', 'profile_id', 'profile_image',
                  'painting', 'created_at', 'updated_at', 'content']


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view
    """
    post = serializers.ReadOnlyField(source='painting.id')
