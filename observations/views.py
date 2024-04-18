from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Observation
from .serializers import ObservationSerializer


class ObservationList(generics.ListCreateAPIView):
    """
    API endpoint that allows observations to be viewed or created.

    * Requires authentication for creating observations to ensure that each
      observation is associated with a user.
    * Any authenticated or unauthenticated user can view the list of
    observations.
    """
    serializer_class = ObservationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Observation.objects.all()

    def perform_create(self, serializer):
        """
        Save the new observation instance, setting the owner to the user who
        made the request. This customization ensures that observations are
        always associated with the logged-in user who creates them.
        """
        serializer.save(owner=self.request.user)


class ObservationDetail(generics.RetrieveDestroyAPIView):
    """
    API endpoint that allows a specific observation to be retrieved or deleted.

    * Only the owner of an observation can delete it.
    * All authenticated users can view the details of any observation.
    * Uses the IsOwnerOrReadOnly permission to ensure that only the owner can
    perform delete operations, protecting the integrity of user data.
    """
    serializer_class = ObservationSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Observation.objects.all()
