import unittest
from app.number import Number

class TestNumber(unittest.TestCase):

    def test_dummy(self):
        self.assertTrue(True, "True is True")

        # self.assertEqual(1, 2, "This should cause a failure")

    def test_value(self):
        n = Number()
        self.assertEqual(n.value, 0, "The default value should be 0")

        n2 = Number(10)
        self.assertEqual(n2.value, 10, "Constructor sets the value")

    def test_random(self):
        r = Number.random()

        self.assertIsInstance(r, Number, "Number.random() returns a Number object")

        Number.lower_bound = 2000
        Number.upper_bound = 2005

        r2 = Number.random()

        self.assertGreaterEqual(r2.value, 2000, "Bounds are followed")
        self.assertLess(r2.value, 2005, "Bounds are followed")