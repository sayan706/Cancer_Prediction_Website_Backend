from django.contrib import admin
from django.urls import path,include
from .views import breastViewSet,lungViewSet,test
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'breasts',breastViewSet)
router.register(r'lungs',lungViewSet)


urlpatterns = [
    path('',include(router.urls))
    
]