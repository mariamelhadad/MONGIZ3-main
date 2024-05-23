from django.urls import path
from . import views

urlpatterns = [
    path('eductional_data/', views.Educational_State.as_view(), name='eductional_data'),
    

]
