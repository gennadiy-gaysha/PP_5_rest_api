from rest_framework import serializers
from .models import Painting


class PaintingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    artist_name = serializers.ReadOnlyField(source='owner.profile.name')
    is_owner = serializers.SerializerMethodField()
    orientation = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError('Image size is larger than 2MB!')
        if value.image.width > 4096:
            raise serializers.ValidationError('Image width is larger than '
                                              '4096px!')
        if value.image.height > 4096:
            raise serializers.ValidationError('Image height is larger than '
                                              '4096px!')
        return value


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
