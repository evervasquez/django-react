from rest_framework import serializers

from negoapps.app.discount.models import Discount


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('id', 'code', 'condition', 'value', 'date_from', 'limit')
