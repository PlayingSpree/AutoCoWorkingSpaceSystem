"""Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# TEMP for file serving
from django.conf.urls.static import static
from django.conf import settings

from authapp.views import FacebookLogin, GoogleLogin

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api-auth/', include('rest_framework.urls')),

                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),

                  path('auth/', include('dj_rest_auth.urls')),
                  path('auth/registration/', include('dj_rest_auth.registration.urls')),
                  path('auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
                  path('auth/google/', GoogleLogin.as_view(), name='google_login'),
                  path('auth/', include('authapp.urls')),

                  path('coworkingspace/', include('coworkingspace.urls')),
                  path('meetingroom/', include('meetingroom.urls')),
                  path('iot/', include('iot.urls')),
                  path('payment/', include('payment.urls')),
                  path('feedback/', include('feedback.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # TEMP for file serving
