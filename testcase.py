import unittest




class Test(unittest.TestCase):  # Test case created
    def test_firstTest(self):   # Test Method defined
        print('This is my first unit test case')


if __name__ == '__main__':  # To make the code run call the main method from the unit test module
    unittest.main()