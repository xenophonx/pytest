import unittest
import inspect

def add(x,y):
    print("\n We are in custom made function add:"+ inspect.stack()[0][3])
    return x+y

class TestClass03(unittest.TestCase):
    def test_case01(self):
        print("\n Running test methode:"+ inspect.stack()[0][3])
        self.assertEqual(add(2,3),5)
    def test_case02(self):
        my_var= 3.14
        print("\n Running test methode:"+ inspect.stack()[0][3])
        self.assertTrue(isinstance(my_var,float))
    def test_case03(self):
        print("\n Running test methode:" + inspect.stack()[0][3])
        self.assertEqual(add(2,2),5)
    def test_case04(self):
        print("\n Running test methode:"+inspect.stack()[0][3])
        my_var =3.14
        self.assertTrue(isinstance(my_var,int))

if __name__ == '__main__':
    unittest.main(verbosity=2)