from rest_framework import generics, filters
from .serializers import ProfileSerializer
from .models import Profile
from drf_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend


class ProfileList(generics.ListAPIView):
    """
    API endpoint for listing user profiles. This view enhances the list
    functionality by including counts of paintings, followers, and following
    for each profile, and supports ordering and filtering based on these
    counts and relationship creation times.

    Filters allow for finding profiles by specific relationship criteria, such
    as profiles that follow a particular user or are followed by a specific
    user.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        paintings_count=Count('owner__painting', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')

    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]

    ordering_fields = ['paintings_count', 'followers_count', 'following_count',
                       'owner__following__created_at',
                       'owner__followed__created_at',
                       ]

    filterset_fields = [
        # filter user profiles that  follow a user with a given profile_id.
        'owner__following__followed__profile',
        # get all profiles that are followed by a profile, given its id
        'owner__followed__owner__profile'
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    API endpoint for retrieving and updating a single user profile. This view
    also annotates the profile with the counts of paintings, followers,
    and following. Only the owner of the profile has the permission to
    update it, ensuring data integrity and privacy.

    Annotation provides real-time counts for the related data, making the
    profile data rich and useful without additional queries.
    """
    serializer_class = ProfileSerializer
    # queryset = Profile.objects.all()
    queryset = Profile.objects.annotate(
        paintings_count=Count('owner__painting', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')
    permission_classes = [IsOwnerOrReadOnly]
