from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    email = serializers.ReadOnlyField(source='owner.email')
    # SerializerMethodField - is a type of field that is used in DRF serializers
    # to add custom fields to our serialized data, where the value of the field
    # is computed by a method on the serializer class SerializerMethodField: This
    # is a read-only field. It is used in a serializer to include some custom or
    # computed data in the serialization output.
    # Dynamic Content: The content of this field is not directly taken from the
    # model instance. It's determined by a method we define on the serializer.
    is_owner = serializers.SerializerMethodField()

    # To provide a value for a SerializerMethodField, we define a method on the
    # serializer class with a specific naming pattern: get_<field_name>.
    # For our field is_owner, the method should be named get_is_owner.
    # Method Implementation: This method takes an instance of the model being
    # serialized (in this case, an instance of a Profile) and returns the value
    # that should be assigned to the is_owner field in the serialized representation.
    # The value for is_owner is determined by the get_is_owner method. This method
    # takes the profile object (obj) as its argument.
    def get_is_owner(self, obj):
        # The method first retrieves the current HTTP request from the serializer context
        request = self.context['request']
        # The method compares the user making the request (request.user)
        # with the owner of the profile (obj.owner). If they are the same, it
        # means the current user is the owner of the profile.
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name', 'bio',
            'home_country', 'gender', 'birthdate', 'image', 'email', 'is_owner',
        ]
