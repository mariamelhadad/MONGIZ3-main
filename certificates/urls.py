from django.urls import path
from . import views
urlpatterns = [
    path("Personal_Info/",views.Personal_Info.as_view(),name="Personal_Info"),
    path("Expereince/",views.Expereince.as_view(),name="Expereince"),
    path("Technical_Skills/",views.Technical_Skills.as_view(),name="Technical_Skills"),
    path("Education/",views.Education.as_view(),name="Education"),
    path("Contact_Info/",views.Contact_Info.as_view(),name="Contact_Info")
]

