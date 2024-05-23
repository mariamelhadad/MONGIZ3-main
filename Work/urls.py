from django.urls import path
from . import views

urlpatterns = [
    path('Work/', views.work.as_view(), name='Work_career')
]
