import unittest
from approcci_lcs.Ricorsivo import Ricorsivo


class TestRicorsivo(unittest.TestCase):
    def test_corretto_funzionamento(self):
        ric = Ricorsivo('KAPBCDEFGHII', 'ABADRMMMMMHUBCDEFGHIKI')

        correct_lcs = 'ABCDEFGHII'
        correct_lcs_length = 10

        ric.lcs()

        self.assertEqual(ric.get_lcs_length(), correct_lcs_length)
        #self.assertEqual(ric.get_lcs_string(), correct_lcs)


if __name__ == '__main__':
    unittest.main()
