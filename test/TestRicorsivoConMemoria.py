import unittest

from approcci_lcs import RicorsivoConMemorizzazione


class TestRicorsivoConMemoria(unittest.TestCase):
    def test_funzionamento(self):
        result = RicorsivoConMemorizzazione.get_lcs('KAPCDEGMHIII', 'AADRMMHUBCDEGHIKI')

        correct_lcs = 'ACDEGHII'
        correct_lcs_length = 8

        self.assertEqual(result, correct_lcs_length)


if __name__ == '__main__':
    unittest.main()
