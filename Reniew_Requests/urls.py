from django.urls import path
from . import views
urlpatterns = [
    path('reniew_personal_id_card/',views.personal_id_card.as_view(),name='reniew_personal_id_card'),
    path('reniew_personal_driving_license/',views.personal_driving_license.as_view(),name='reniew_personal_driving_license')
]
