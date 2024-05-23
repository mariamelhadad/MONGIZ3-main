from django.urls import path
from . import views
urlpatterns = [
    path('medical_history/', views.medical_history.as_view(), name='medical_history'),
]
