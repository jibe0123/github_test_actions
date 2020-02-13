import unittest
from app import add


class AddTest(unittest.TestCase):

    def test_add(self):
        test_number_a = 3
        test_number_b = 6

        test_result = 9

        result = add(test_number_a, test_number_b)

        self.assertEqual(result, test_result)


if __name__ == '__main__':
    unittest.main()
