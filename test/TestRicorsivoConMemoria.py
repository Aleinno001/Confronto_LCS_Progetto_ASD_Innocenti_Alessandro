import unittest

from approcci_lcs.RicorsivoConMemorizzazione import RicorsivoConMemorizzazione


class TestRicorsivoConMemoria(unittest.TestCase):
    def test_funzionamento(self):
        ric = RicorsivoConMemorizzazione('ABCDEFGHII', 'ABADRMMMMMHUBCDEFGHIKI')

        correct_lcs = 'ABCDEFGHII'
        correct_lcs_length = 10

        ric.lcs()

        self.assertEqual(ric.get_lcs_string(), correct_lcs)
        self.assertEqual(ric.get_lcs_length(), correct_lcs_length)


if __name__ == '__main__':
    unittest.main()
