from django.urls import path
from .views import diagnosis, result, old_diagnosis, check_image_quality, is_retinopathy_present, severity_level


urlpatterns = [
    path('', diagnosis, name='diagnosis'),
    path('check_image_quality', check_image_quality, name='check_image_quality'),
    path('is_retinopathy_present', is_retinopathy_present, name='is_retinopathy_present'),
    path('severity_level', severity_level, name='severity_level'),
    path('result/<int:pk>/', result, name='result'),
    path('old_diagnosis', old_diagnosis, name='old_diagnosis'),
]
