import django_filters
from django.db.models import Q

from utilities.filters import NameSlugSearchFilterSet

from sdns.models import Register


class RegisterFilter(NameSlugSearchFilterSet):
    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    class Meta:
        model = Register
        fields = [
            'ip',
            'host',
            'domain',
        ]

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset

        qs_filter = (
            Q(ip__icontains=value)
            | Q(host__icontains=value)
            | Q(domain__icontains=value)
        )

        return queryset.filter(qs_filter)