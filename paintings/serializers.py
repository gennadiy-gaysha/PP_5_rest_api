from rest_framework import serializers
from .models import Painting
from observations.models import Observation


class PaintingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Painting model that includes serialization for painting
    attributes along with additional fields and custom validation and
    retrieval methods.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    artist_name = serializers.ReadOnlyField(source='owner.profile.name')
    is_owner = serializers.SerializerMethodField()
    orientation = serializers.SerializerMethodField()
    creation_year = serializers.IntegerField(min_value=1000, max_value=9999)
    observation_id = serializers.SerializerMethodField()
    observations_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_creation_year(self, value):
        """
        Validates that the provided year for a painting's creation falls within
        an acceptable range.
        """
        if not 1000 <= value <= 9999:
            raise serializers.ValidationError('Enter a valid year')
        return value

    def validate_image(self, value):
        """
        Validates the size and dimensions of the uploaded image for a painting.
        """
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
        """
        Checks if the current request user is the owner of the painting.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_orientation(self, obj):
        """
        Determines the orientation of the painting based on its width and
        height.
        """
        if obj.width > obj.height:
            return 'Horizontal'
        elif obj.width < obj.height:
            return 'Vertical'
        else:
            return 'Square'

    def get_observation_id(self, obj):
        """
        Retrieves the ID of the observation made by the current request user
        for the painting.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            observation = Observation.objects.filter(owner=user,
                                                     painting=obj
                                                     ).first()
            return observation.id if observation else None
        return None

    class Meta:
        model = Painting
        fields = [
            'id', 'owner', 'profile_id', 'is_owner', 'profile_image',
            'created_at', 'updated_at', 'artist_name', 'title',
            'creation_year', 'technique', 'theme', 'width', 'height',
            'orientation', 'price', 'image', 'observation_id',
            'observations_count', 'comments_count',
        ]
