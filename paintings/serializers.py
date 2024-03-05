from rest_framework import serializers
from .models import Painting


class PaintingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    artist_name = serializers.ReadOnlyField(source='owner.profile.name')
    is_owner = serializers.SerializerMethodField()
    orientation = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_orientation(self, obj):
        """
        Determines the orientation of the painting based on its width and height.
        """
        if obj.width > obj.heigh:
            return 'Landscape'
        elif obj.width < obj.heigh:
            return 'Portrait'
        else:
            return 'Square'

    class Meta:
        model = Painting
        fields = [
            'id', 'owner', 'profile_id', 'profile_image', 'created_at',
            'updated_at', 'artist_name', 'is_owner', 'title',
            'year_created', 'technique', 'theme', 'width', 'height',
            'orientation', 'price', 'availability',
        ]
