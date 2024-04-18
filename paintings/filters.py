from django_filters import rest_framework as df_filters, ChoiceFilter
from .models import Painting
from django.db.models import F


class PaintingFilter(df_filters.FilterSet):
    """
    FilterSet for the Painting model. Provides filtering options for paintings
    by theme, technique, orientation, and specific user-based filters such
    as user's favorites, watchlist, and owned paintings.
    """
    ORIENTATION_CHOICES = [
        ('Horizontal', 'Horizontal'),
        ('Vertical', 'Vertical'),
        ('Square', 'Square'),
    ]

    orientation = ChoiceFilter(choices=ORIENTATION_CHOICES,
                               method='filter_orientation')

    class Meta:
        model = Painting
        fields = ['theme', 'technique',
                  # User's Faves
                  'owner__followed__owner__profile',
                  # User's Watchlist
                  'observations__owner__profile',
                  # User's Paintings
                  'owner__profile']

    def filter_orientation(self, queryset, name, value):
        """
        Custom method to filter the queryset based on the orientation of
        paintings. Orientation is determined by comparing the width and
        height of each painting.
        """
        if value.lower() == 'horizontal':
            return queryset.filter(width__gt=F('height'))
        elif value.lower() == 'vertical':
            return queryset.filter(width__lt=F('height'))
        elif value.lower() == 'square':
            return queryset.filter(width=F('height'))
        return queryset
