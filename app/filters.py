import django_filters
from .models import Sensores, Ambientes, Historico

class sensorFiltro(django_filters.FilterSet):
    tipoSensor = django_filters.CharFilter(field_name='sensor__sensor', lookup_expr='iexact')
    def filter_queryset(self, queryset):
        filtro = super().filter_queryset(queryset)
        ana  = self.data.get('timestamp', None)
        if ana:
            ht = Historico.objects.filter(valor__gte=int(ana))
            filtro = filtro.filter(id__in=ht.values_list('sensor_id', flat=True))
        
        return filtro
    class Meta:
        model = Sensores
        fields = ['sensor']

class ambienteFiltro(django_filters.FilterSet):
    sigAmbiente = django_filters.NumberFilter(field_name='sig__sig')

    class Meta:
        model = Ambientes
        fields = ['sig']


class dataSensor(django_filters.FilterSet):
    data = django_filters.DateFilter(field_name='timestamp', lookup_expr='date')

    class Meta:
        model = Historico
        fields = ['timestamp']