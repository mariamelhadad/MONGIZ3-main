from . import views
from django.urls import path
urlpatterns = [
    path('technical_report/',views.report.as_view(),name='report'),
]
