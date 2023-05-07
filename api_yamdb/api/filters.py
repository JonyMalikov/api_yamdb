import django_filters
from django_filters import CharFilter, NumberFilter
from reviews.models import Title


class TitleFilter(django_filters.FilterSet):
    """Класс для создания фильтров."""
    name = django_filters.CharFilter(
        field_name='name', lookup_expr='iexact')
    genre = CharFilter(
        field_name='genre__slug', lookup_expr='iexact')
    category = CharFilter(
        field_name='category__slug', lookup_expr='iexact')
    year = NumberFilter(
        field_name='year', lookup_expr='iexact')

    class Meta:
        model = Title
        fields = ('name', 'year', 'genre__slug', 'category__slug')
