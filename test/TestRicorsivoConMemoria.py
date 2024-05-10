import unittest

from approcci_lcs.RicorsivoConMemorizzazione import RicorsivoConMemorizzazione


class TestRicorsivoConMemoria(unittest.TestCase):
    def test_funzionamento(self):
        ricm = RicorsivoConMemorizzazione('KAPCDEGMHIII', 'AADRMMHUBCDEGHIKI')

        correct_lcs = 'ACDEGHII'
        correct_lcs_length = 8

        ricm.lcs()

        self.assertEqual(ricm.get_lcs_string(), correct_lcs)
        self.assertEqual(ricm.get_lcs_length(), correct_lcs_length)


if __name__ == '__main__':
    unittest.main()
