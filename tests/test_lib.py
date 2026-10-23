import unittest
from lib import f

class T(unittest.TestCase):
    def test_f(self):
        self.assertEqual(f(), 1)
