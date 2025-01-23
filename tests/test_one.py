import unittest

from a_dir.a import function1, function2  # Import the functions you want to test

class TestA(unittest.TestCase):

    def test_function1(self):
        # Test cases for function1
        self.assertEqual(function1(1, 2), 3)
       

    def test_function2(self):
        # Test cases for function2
        self.assertTrue(function2('hello'))
      

if __name__ == '__main__':
    unittest.main()