from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Observation
from .serializers import ObservationSerializer

class ObservationList(generics.ListCreateAPIView):
    serializer_class = ObservationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Observation.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ObservationDetail(generics.RetrieveDestroyAPIView):
    serializer_class = ObservationSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Observation.objects.all()