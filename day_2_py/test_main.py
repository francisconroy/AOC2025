from unittest import TestCase

from main import is_item_valid_advanced


class Test(TestCase):
    def test_is_item_valid_advanced(self):
        self.assertTrue(is_item_valid_advanced(1188511880))
