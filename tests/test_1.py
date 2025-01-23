import unittest 


class Test_1(unittest.TestCase):

    def test_true(self):
        self.assertEqual(1, 1)

    def test_false(self):
        self.assertEqual(0, 1)


if __name__ =='__main__':
    unittest.main()

