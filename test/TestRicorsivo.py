import unittest
from approcci_lcs import get_ric_lcs


class TestRicorsivo(unittest.TestCase):
    def test_corretto_funzionamento(self):
        result = get_ric_lcs('KAPCDEGMHIII', 'AADRMMHUBCDEGHIKI')

        correct_lcs = 'ACDEGHII'
        correct_lcs_length = 8

        self.assertEqual(result, correct_lcs_length)


if __name__ == '__main__':
    unittest.main()
