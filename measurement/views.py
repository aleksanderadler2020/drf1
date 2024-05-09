# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


# Создать датчик. Указываются название и описание датчика.
# Изменить датчик. Указываются название и описание.
# Получить список датчиков. Выдаётся список с краткой информацией по датчикам: ID, название и описание.
class SensorListCreateView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# Добавить измерение. Указываются ID датчика и температура
class MeasurementListCreateView(generics.ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

# Получить информацию по конкретному датчику. Выдаётся полная информация по датчику:
# ID, название, описание и список всех измерений с температурой и временем.
class SensorDetailListCreateView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
