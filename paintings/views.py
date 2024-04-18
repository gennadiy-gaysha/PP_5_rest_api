from rest_framework import generics, permissions, filters
from .serializers import PaintingSerializer
from .models import Painting
from drf_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django_filters import rest_framework as df_filters
from .filters import PaintingFilter


class PaintingList(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating paintings. It supports searching,
    ordering, and filtering.

    Paintings are annotated with the count of comments and observations they
    have, which can also be used for ordering the results. Filters include
    custom filters defined in PaintingFilter.
    """
    serializer_class = PaintingSerializer
    queryset = Painting.objects.annotate(
        comments_count=Count('comment', distinct=True),
        observations_count=Count('observations', distinct=True)
    ).order_by('-created_at')

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [filters.OrderingFilter, filters.SearchFilter,
                       df_filters.DjangoFilterBackend]

    filterset_class = PaintingFilter
    search_fields = ['owner__profile__name', 'title']
    ordering_fields = ['observations_count', 'comments_count',
                       'observations__created_at', 'price']

    def perform_create(self, serializer):
        """
        Customizes the creation of a painting by automatically assigning
        the logged-in user as the owner of the painting.
        """
        serializer.save(owner=self.request.user)


class PaintingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting a single painting.

    The painting instance is annotated with the count of comments and
    observations, which can be used in the retrieval of detailed data. The
    permissions ensure that only the owner of the painting can update or
    delete it.
    """
    serializer_class = PaintingSerializer
    # queryset = Painting.objects.all()
    queryset = Painting.objects.annotate(
        comments_count=Count('comment', distinct=True),
        observations_count=Count('observations', distinct=True)
    ).order_by('-created_at')
    permission_classes = [IsOwnerOrReadOnly]
