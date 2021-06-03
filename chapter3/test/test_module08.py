import unittest
import test_me 

class TestClass09(unittest.TestCase):
    def test_case01(self):
        self.assertEqual(test_me.add(4,5),9)
        print('\n In test_Case01()')
    
    def test_case02(self):
        self.assertEqual(test_me.mul(2,2),4)
        print('\n In test_case02()')

if __name__ == '__main__':
    unittest.main()
       
    

