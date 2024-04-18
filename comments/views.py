from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend


class CommentList(generics.ListCreateAPIView):
    """
    API endpoint that allows comments to be viewed or created.

    * Requires authentication for posting comments.
    * Any user can view comments.
    * Supports filtering comments by the 'painting' field to retrieve all comments associated with a specific painting.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        # retrieves all the comments associated with a given painting
        'painting'
    ]

    def perform_create(self, serializer):
        """
        Save the new comment instance, setting the owner to the user who made
        the request.
        """
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a comment to be retrieved, updated, or deleted.

    * The owner of the comment can update or delete it.
    * Other authenticated users can view the comment details.
    * Permissions are handled by the IsOwnerOrReadOnly custom permission class.
    """
    serializer_class = CommentDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
