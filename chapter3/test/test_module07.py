import unittest

class TestClass08(unittest.TestCase):
    
    def test_case01(self):
        self.assertTrue('PYTHON'.isupper())
        print('\n In test_case01() methode.')
    def test_case02(self):
        self.assertTrue('Python'.isupper())
        print('\n In test_case02() methode.')
    
    def test_case03(self):
        self.assertTrue(True)
        print('\n In test_case03() methode')