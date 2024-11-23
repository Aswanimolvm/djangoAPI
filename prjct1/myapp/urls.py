from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings

from myapp.views import Userviewset
from rest_framework.routers import DefaultRouter 
router=DefaultRouter()
router.register('CustomUser',Userviewset)


urlpatterns = [
    path('register/',userregister.as_view(),name="register"),
    path('api/token/',TokenObtainPairView.as_view()),
    path('api/token/refresh',TokenRefreshView.as_view()),
    path('profile/',profile.as_view(),name="profile"),
]
