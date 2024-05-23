from django.urls import path
from . import views

urlpatterns = [
    path('Reports/', views.Report.as_view(), name='Reports')
]
