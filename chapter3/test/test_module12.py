import sys
import unittest

class TestClass13(unittest.TestCase):
    
    @unittest.skipUnless(sys.platform.startswith("win"),"Requires windows")
    def test_case01(self):
        '''Test will run in a windows Os'''
        pass
    
    @unittest.skip("Demostrating unconditional skipping")
    def test_case02(self):
        self.fail("FATAL")
    
    @unittest.skipUnless(sys.platform.startswith("darwin"),"Requires MacOs")
    def test_case03(self):
        '''Test will run in a Mac Os'''
        print('test_case03() specific to MacOs had run')
        

