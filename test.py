import unittest
from module import creation_aliment

class GiftTestCase(unittest.TestCase):
    def test_creation_aliment(self):
        fruit = creation_aliment('fruit')
        self.assertEqual(fruit["poid"],1)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    import unittest
    unittest.main()
