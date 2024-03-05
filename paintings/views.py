from rest_framework import generics, permissions
from .serializers import PaintingSerializer
from .models import Painting
from drf_api.permissions import IsOwnerOrReadOnly


class PaintingList(generics.ListCreateAPIView):
    serializer_class = PaintingSerializer
    queryset = Painting.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PaintingDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PaintingSerializer
    queryset = Painting.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
