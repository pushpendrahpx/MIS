from django.urls import path, include
from . import views
from django.contrib.auth.views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register('userinfo', views.UserInfoView)
urlpatterns = [
    path('', include(router.urls)),
    path('api/', views.json_create, name='json')
]
