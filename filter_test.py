import unittest
from filter import slash_access

class TestFilter(unittest.TestCase):
    def test_filter(self):
        
        my_object = {"a":{"b":{"c":"d"}}}
        res =  slash_access(my_object,"a/b")
        self.assertEqual(res, {'c': 'd'})
      
    def test_error(self):
        my_object = {"a":{"b":{"c":"d"}}}
        with self.assertRaises(BaseException):
           slash_access(my_object,"a/c")
       

if __name__ == '__main__':
    unittest.main()