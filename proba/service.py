from django_filters import rest_framework as filters
from .models import Prob


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProbFilter(filters.FilterSet):
    dolznoct = CharFilterInFilter(field_name='dolznoct__sotrudnik', lookup_expr='in')

    class Meta:
        model = Prob
        fields = ['dolznoct']
