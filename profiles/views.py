from rest_framework import generics, filters
from .serializers import ProfileSerializer
from .models import Profile
from drf_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count



class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer
    # queryset = Profile.objects.all()
    queryset = Profile.objects.annotate(
        paintings_count=Count('owner__painting', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')
    filter_backends = [filters.OrderingFilter]
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
    serializer_class = ProfileSerializer
    # queryset = Profile.objects.all()
    queryset = Profile.objects.annotate(
        paintings_count=Count('owner__painting', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')
    permission_classes = [IsOwnerOrReadOnly]
