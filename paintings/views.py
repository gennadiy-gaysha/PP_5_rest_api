from rest_framework import generics, permissions, filters
from .serializers import PaintingSerializer
from .models import Painting
from drf_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django_filters import rest_framework as df_filters
from .filters import PaintingFilter


class PaintingList(generics.ListCreateAPIView):
    serializer_class = PaintingSerializer

    # queryset = Painting.objects.all()
    # queryset = Painting.objects.annotate(
    #     comments_count=Count('comment', distinct=True),
    #     observations_count=Count('observations', distinct=True)
    # ).order_by('-created_at')

    def get_queryset(self):
        """
        Optionally restricts the returned paintings to a given theme,
        by filtering against a `theme` query parameter in the URL.
        """
        queryset = Painting.objects.annotate(
            comments_count=Count('comment', distinct=True),
            observations_count=Count('observations', distinct=True)
        ).order_by('-created_at')
        theme = self.request.query_params.get('theme', None)
        if theme is not None:
            queryset = queryset.filter(theme=theme)
        return queryset

    filter_backends = [filters.OrderingFilter, filters.SearchFilter, df_filters.DjangoFilterBackend]
    filterset_class = PaintingFilter
    search_fields = ['owner__profile__name', 'title']
    ordering_fields = ['observations_count', 'comments_count',
                       'observations__created_at']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PaintingDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PaintingSerializer
    # queryset = Painting.objects.all()
    queryset = Painting.objects.annotate(
        comments_count=Count('comment', distinct=True),
        observations_count=Count('observations', distinct=True)
    ).order_by('-created_at')
    permission_classes = [IsOwnerOrReadOnly]
