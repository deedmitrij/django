"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.conf.urls import url, include
from .router import router
from rest_framework.authtoken import views as drf_views
from test_project import views
from django.views.generic import TemplateView


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', drf_views.obtain_auth_token),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', login_required(TemplateView.as_view(template_name='user_weight.html'))),
    url(r'^', include('test_project.urls')),
]
# from django.conf.urls import include, url
# from django.contrib import admin
#
#
# urlpatterns = [
#     url(r'^/', include('user.urls')),
#     url(r'^admin/', admin.site.urls)]
