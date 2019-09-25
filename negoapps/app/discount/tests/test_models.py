from django.test import TestCase

from negoapps.app.discount.models import Discount, CONDITIONS_DISCOUNT


class DiscountModelTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.code = "TETE526272HND"
        self.model = Discount.objects.create(
            code=self.code,
            condition=CONDITIONS_DISCOUNT[0][0],
            value=12
        )

    def test_discount_str(self):
        model = Discount.objects.last()
        self.assertEqual(self.code, model.__str__())
