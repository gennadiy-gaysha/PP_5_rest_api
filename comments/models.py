from django.db import models
from django.contrib.auth.models import User
from paintings.models import Painting


class Comment(models.Model):
    """
    Represents a comment made by a user on a painting. This model maintains a
    relationship to both the User model and the Painting model, indicating
    ownership and association respectively.

    Meta:
        ordering: Orders comments by creation time in descending order, so the
        newest comments appear first.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    painting = models.ForeignKey(Painting, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
