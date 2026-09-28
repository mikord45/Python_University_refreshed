import unittest

class SorteTest(unittest.TestCase):
    def setUp(self):
        self.l = [4,2,1,3]
    def test_sorted_list(self):
        self.assertEqual(sorted(self.l), [1,2,3,4])
    def test_sorted_int(self):
        self.assertRaises(TypeError, sorted, 78)

suite = unittest.TestLoader().loadTestsFromTestCase(SorteTest)
unittest.TextTestRunner(verbosity=2).run(suite)