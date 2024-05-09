from django.urls import path

from measurement.views import SensorListCreateView, MeasurementListCreateView, SensorDetailListCreateView

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view()),
    path('measurements/', MeasurementListCreateView.as_view()),
    path('sensors_detail/', SensorDetailListCreateView.as_view()),
]
