from django_filters import rest_framework as df_filters, ChoiceFilter
from .models import Painting
from django.db.models import F


class PaintingFilter(df_filters.FilterSet):
    ORIENTATION_CHOICES = [
        ('Landscape', 'Landscape'),
        ('Portrait', 'Portrait'),
        ('Square', 'Square'),
    ]

    orientation = ChoiceFilter(choices=ORIENTATION_CHOICES,
                               method='filter_orientation')

    class Meta:
        model = Painting
        fields = ['theme', 'technique', 'availability',
                  # User's Faves
                  'owner__followed__owner__profile',
                  # User's Watchlist
                  'observations__owner__profile',
                  # User's Paintings
                  'owner__profile']

    def filter_orientation(self, queryset, name, value):
        """
        Filters the queryset based on painting orientation.
        Assumes 'Landscape', 'Portrait', and 'Square' as valid values for 'value'.
        """
        if value.lower() == 'Landscape':
            return queryset.filter(width__gt=F('height'))
        elif value.lower() == 'portrait':
            return queryset.filter(width__lt=F('height'))
        elif value.lower() == 'square':
            return queryset.filter(width=F('height'))
        return queryset
