import unittest
from approcci_lcs.ForzaBruta import ForzaBruta


class MyTestCase(unittest.TestCase):
    def test_something(self):
        fb = ForzaBruta('ABCD', 'ACBAD')

        correct_lcs = 'ABD'

        result = fb.lcs()

        self.assertEqual(result, correct_lcs)


if __name__ == '__main__':
    unittest.main()
