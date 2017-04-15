#encoding=utf-8

import unittest
import Calc

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.c = Calc.Calc()
        print "setup completed!"
    def test_add(self):
        result = self.c.add(1, 2,3,4,5)
        self.assertEqual(result, 15)
    def test_sub(self):
        result = self.c.sub(10,5,2,1)
        assert result == 2
    def test_mul(self):
        result = self.c.mul(1, 2, 3, 4, 5)
        self.assertTrue(result == 10)
    def test_div(self):
        result = self.c.div(20, 2, 2, 1)
        self.assertTrue(result == 5)
    def tearDown(self):
        print 'teardown completed!'

if __name__ == '__main__':
    unittest.main()