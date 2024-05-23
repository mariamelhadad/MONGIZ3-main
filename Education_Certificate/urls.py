from django.urls import path
from . import views
urlpatterns = [
    path('eductional_data_certification/', views.Educational_Certification.as_view(), name='eductional_data_certification'),
]
