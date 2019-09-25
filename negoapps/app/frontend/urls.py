from django.urls import path, include

from negoapps.app.discount.views import DiscountViewSet
from . import views

urlpatterns = [
    path('', views.index),
]
