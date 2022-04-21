"""b2c URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from rest_framework import permissions
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .env import env
from accounts.views import index as accountViewSet

schema_view = get_schema_view( 
    openapi.Info( 
        title="B2C API with Django", 
        default_version="v1", 
        description="B2C API 문서", 
        terms_of_service="https://www.google.com/policies/terms/", 
        contact=openapi.Contact(name="b2c", email="b2c@b2c.com"), 
        license=openapi.License(name="B2C License"), 
    ), 
    public=True, 
    permission_classes=(permissions.AllowAny,), 
)

router_user = routers.DefaultRouter()
router_user.register(r"accounts", accountViewSet, basename="accounts")


urlpatterns = [
    path("test/", include(router_user.urls))
]

if env.DEBUG:
    urlpatterns += [
        path('admin/', admin.site.urls),
        #path("accounts/", include(router_user.urls)),
        path(
            "swagger-b2c<str:format>",
            schema_view.without_ui(cache_timeout=0),
            name="swaager-b2c-json",
        ),
        path(
            "swagger-b2c/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="swagger-b2c",
        ),
        path(
            "redoc-b2c/",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="redoc-b2c",
        ),
        
    ]
