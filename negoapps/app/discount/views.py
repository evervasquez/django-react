from rest_framework import generics

from negoapps.app.discount.mixins import DefaultViewSetMixin, ModelViewSet
from negoapps.app.discount.models import Discount
from negoapps.app.discount.serializers import DiscountSerializer


# class DiscountViewSet(DefaultViewSetMixin, ModelViewSet):
class DiscountViewSet(ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
