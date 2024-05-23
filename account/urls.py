from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.registerationview.as_view(),name='register'),
    path('login/',views.login.as_view(),name='login'),
    path('profile/',views.userprofile.as_view(),name='profile'),
    path('changepassword/',views.changepassword.as_view(),name='changepassword'),
    path('forget_password/',views.forget_password.as_view(),name='forget_password'),
    path('reset_password/<uid>/<token>/',views.userpasswordreset.as_view(),name='reset_password'),
    path('update_user/',views.Update_User.as_view(),name='update_user'),
]
