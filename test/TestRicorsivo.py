import unittest
from approcci_lcs.Ricorsivo import Ricorsivo


class TestRicorsivo(unittest.TestCase):
    def test_corretto_funzionamento(self):
        ric = Ricorsivo('ABCDEFGHI', 'ABADRMMMMMHUBCDEFGHI')

        correct_lcs = 'ABCDEFGHI'

        result = ric.lcs()

        self.assertEqual(result, correct_lcs)


if __name__ == '__main__':
    unittest.main()
