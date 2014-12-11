from battles.pacific import models, serializers
from rest_framework import generics
import django_filters

class IntegerListFilter(django_filters.Filter):
    def filter(self, queryset, value):
        if value not in (None, ''):
            integers = [int(v) for v in value.split(',')]
            return queryset.filter(**{'{}__{}'.format(self.name, self.lookup_type):integers})
        return queryset

class BattleFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.Battle
        fields = ['id', 'name']

class PIFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.PointInterest
        fields = ['id', 'name', 'desc']

class BattleCollection(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Battle.objects.all()
    serializer_class = serializers.BattleSerializer
    filter_class = BattleFilter

class PICollection(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.PointInterest.objects.all()
    serializer_class = serializers.PISerializer
    filter_class = PIFilter

