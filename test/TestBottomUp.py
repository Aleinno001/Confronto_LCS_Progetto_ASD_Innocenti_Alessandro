import unittest

from approcci_lcs.BottomUp import BottomUp


class TestBottomUp(unittest.TestCase):
    def test_funzionamento(self):
        bu = BottomUp('KAPCDEGMHIII', 'AADRMMHUBCDEGHIKI')

        correct_lcs = 'ACDEGHII'
        correct_lcs_length = 8

        bu.lcs()

        self.assertEqual(bu.get_lcs_length(), correct_lcs_length)
        self.assertEqual(bu.get_lcs_string(), correct_lcs)


if __name__ == '__main__':
    unittest.main()
