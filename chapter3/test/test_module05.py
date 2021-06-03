import unittest
import inspect

def setUpModule():
    '''Called ones, before everything else in this module.'''
    print('In setUpModule()...')

def tearDownModule():
    '''Called once, aftre everything in this module.'''
    print('In tearDownModule()...')

class TestClass06(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''Called once before any test in the class'''
        print('In setUpClass()...')

    @classmethod
    def tearDownClass(cls):
        '''Called once after all tests if setUpClass is successful.'''
        print('In tearDownClass()...')
    
    def setUp(self):
        '''called multipe times before every test.'''
        print('In setUp()...')
    
    def tearDown(self):
        '''Called multiple times after every test.'''
        print('In tearDown()...')

    def test_case01(self):
        self.assertTrue('PYTHON'.isupper())
        print('In test_case01()...')

    def test_case02(self):
        self.assertTrue('python'.isupper())
        print('In test_case02()...')




if __name__ == '__main__':
    unittest.main()