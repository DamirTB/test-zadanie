"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Test Zadanie API",
      default_version='v1',
      description="Swagger docs for Test Zadanie API",
   ),
   public=True,
)


urlpatterns = [
    path('swagger/', 
         schema_view.with_ui('swagger', cache_timeout=0), 
         name='schema-swagger-ui'), 
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('api/main/', include('main.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
)
