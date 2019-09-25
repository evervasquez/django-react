
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from negoapps.app.discount.views import DiscountViewSet

router = routers.DefaultRouter(trailing_slash=True)
#router.register(r'inventory/categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('discount/', DiscountViewSet.as_view({'get': 'list'})),
]
