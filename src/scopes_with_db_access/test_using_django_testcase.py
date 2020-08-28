import logging

from django.contrib.auth import get_user_model
from django.test import TestCase


class ReusingDatabaseTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        logging.info('setting up django TestCase')
        cls.user = get_user_model().objects.create(
            username='foobar',
            is_staff=False
        )

    def test_foobar_username(self):
        self.assertEqual(self.user.username, 'foobar')

    def test_foobar_is_not_staff(self):
        self.assertFalse(self.user.is_staff)
