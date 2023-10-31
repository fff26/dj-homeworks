from django_filters import rest_framework as filters
from advertisements.models import AdvertisementStatusChoices
from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at_before = filters.DateFromToRangeFilter()
    status = filters.ChoiceFilter(
        method="filter_status"
    )

    def filter_status(self, queryset, name, value):
        if value == AdvertisementStatusChoices.OPEN:
            return queryset.filter(status=AdvertisementStatusChoices.OPEN)
        elif value == AdvertisementStatusChoices.CLOSED:
            return queryset.filter(status=AdvertisementStatusChoices.CLOSED)
        return queryset

    class Meta:
        model = Advertisement
        fields = ["created_at", "status"]
