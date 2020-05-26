import django_filters
from .models import *
from django_filters import CharFilter


class eventFilter1(django_filters.FilterSet):

    e_title= CharFilter(field_name='e_title', lookup_expr='icontains')

    class Meta:
        model = Events
        fields = ['e_title', 'e_status', 'e_type']

class rsvpFilter1(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = RSVP
        fields = ['name', 'event']