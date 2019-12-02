import unittest
import number


class TestNumber(unittest.TestCase):

    def test_is_prime_7(self):
        self.assertTrue( number.is_prime(7) )

    def test_is_prime_2(self):
        self.assertTrue( number.is_prime(2) )

    def test_is_prime_4(self):
        self.assertFalse( number.is_prime(4) )

class TestELK(unittest.TestCase):

    def test_true(self):
        self.assertTrue( True )
