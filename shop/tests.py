from django.contrib.auth.models import User
from django.test import TestCase

from shop.models import Product, Payment, OrderItem, Order


class TestDataBase(TestCase):
    fixtures = [
        "shop/fixtures/dump.json"
    ]

    def setUp(self):
        self.user = User.objects.get(username='admin')

    def test_user_exists(self):
        users = User.objects.all()
        users_number = users.count()
        user = users.first()
        self.assertEqual(users_number, 1)
        self.assertEqual(user.username, 'admin')
        self.assertTrue(user.is_superuser)

    def test_user_check_password(self):
        self.assertTrue(self.user.check_password('5'))

    def test_all_data(self):
        self.assertGreater(Product.objects.all(), 0)
        self.assertGreater(Payment.objects.all(), 0)
        self.assertGreater(OrderItem.objects.all(), 0)
        self.assertGreater(Order.objects.all(), 0)
