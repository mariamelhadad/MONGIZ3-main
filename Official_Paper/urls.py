from django.urls import path
from . import views

urlpatterns = [
    path('Official_Paper/', views.offcial_papers.as_view(), name='Official_Paper')
]
