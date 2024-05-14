import unittest

from approcci_lcs import get_bottom_up_lcs


class TestBottomUp(unittest.TestCase):
    def test_funzionamento(self):
        result = get_bottom_up_lcs('KAPCDEGMHIII', 'AADRMMHUBCDEGHIKI')

        correct_lcs = 'ACDEGHII'
        correct_lcs_length = 8

        self.assertEqual(result, correct_lcs_length)


if __name__ == '__main__':
    unittest.main()
