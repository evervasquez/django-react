from django.db import models

from negoapps.app.discount.mixins import TimeStampedModel

CONDITIONS_DISCOUNT = [
    ('0', 'Amount'),
    ('1', 'Percentage'),
]


class Discount(TimeStampedModel):
    code = models.CharField(max_length=16)
    condition = models.CharField(max_length=1, choices=CONDITIONS_DISCOUNT, default='1')
    value = models.DecimalField(max_digits=18, decimal_places=2)
    date_from = models.DateField(null=True, blank=True)
    limit = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.code
