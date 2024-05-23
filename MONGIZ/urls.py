"""
URL configuration for MONGIZ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('',include('account.urls')),
    path('', include('Education.urls')),
    path('', include('Education_Certificate.urls')),
    path('', include('Health.urls')),
    path('', include('Medical_History.urls')),
    path('',include('Social.urls')),
    path('',include('Home.urls')),
    path('',include('Official_Paper.urls')),
    path('',include('Work.urls')),
    path('',include('Tecnical_Report.urls')),
    path('',include('certificates.urls')),
    path('',include('Reniew_Requests.urls')),
    path('',include('Messages.urls')),
    path('',include('Reports.urls'))
]


