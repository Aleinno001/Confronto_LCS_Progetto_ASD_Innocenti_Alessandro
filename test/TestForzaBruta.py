import unittest
from approcci_lcs.ForzaBruta import ForzaBruta


class TestForzaBruta(unittest.TestCase):
    def test_corretto_funzionamento(self):
        fb = ForzaBruta('ABCDEFGHI', 'ABADRMMMMMHUBCDEFGHI')

        correct_lcs = 'ABCDEFGHI'

        result = fb.lcs()

        self.assertEqual(result, correct_lcs)


if __name__ == '__main__':
    unittest.main()
