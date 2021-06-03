
import unittest
from  mypackage.mymathlib import *

math_obj = 0
def setUpModule():
    '''Called once at the strt of the module'''
    print('In setUpModule()..!')
    global math_obj
    math_obj = mymathlib()


class TestClass10(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        '''Called once before all other methods'''
        print('In setUpClass() method.')
    
    def setUp(self):
        '''Called  before every test method'''
        print('In setUp() method.')
    
    def Test_Case01(self):
        print('In Test_Case01')
        self.assertEqual(math_obj.add(4,5),9)
    
    def Test_Case02(self):
        print('In Test_Case02()..')
        self.assertEqual(math_obj.mul(2,2),10)
    
    def tearDown(self):
        '''Called once all test methods are ran.'''
        print('In tearDown() method.')
    
    @classmethod
    def tearDownClass(cls):
        '''Called once after all other methods in the class.'''
        print('In tearDownClass().')

def tearDownModule():
    '''Called once at the end of the module'''
    print('In tearDownModule()..!')
    global math_obj
    del math_obj
    
# if __name__ == '__name__':
#     unittest.main()


