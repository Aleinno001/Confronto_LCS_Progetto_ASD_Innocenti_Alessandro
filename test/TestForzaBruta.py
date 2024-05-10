import unittest
from approcci_lcs.ForzaBruta import ForzaBruta


class TestForzaBruta(unittest.TestCase):
    def test_corretto_funzionamento(self):
        fb = ForzaBruta('KAPCDEGMHIII', 'AADRMMHUBCDEGHIKI')

        correct_lcs = 'ACDEGHII'
        correct_lcs_length = 8

        fb.lcs()

        self.assertEqual(fb.get_lcs_length(), correct_lcs_length)
        self.assertEqual(fb.get_lcs_string(), correct_lcs)


if __name__ == '__main__':
    unittest.main()
