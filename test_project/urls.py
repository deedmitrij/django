from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('', admin.site.urls),
    path('', views.measurement, name='index'),
    path('signup/', views.signup, name='signup'),
    path('password_recovery/', views.pass_recovery, name='recovery'),
    path('user_profile/', views.user_profile, name='user_profile')
]