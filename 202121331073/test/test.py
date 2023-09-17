import unittest
import sys
import os
import time
sys.path.append(os.path.dirname(sys.path[0]))
import simhash  # noqa: E402



class Testsimhash(unittest.TestCase):
    #空文本
    def test_empty(self): 
        sc = simhash.simhash_check('test\org_empty.txt','test\org_add_empty.txt')  # noqa: E501
        result = sc.check()
        print('空文本:',result)
        self.assertEqual(result,1)
    #长文本、相似度高
    def test_long_high(self):
        sc = simhash.simhash_check('test\org_long_high.txt','test\org_add_long_high.txt')  # noqa: E501
        result = sc.check()
        print('长文本高相似：',result)
        self.assertTrue(result<100 and result>0)
    #长文本低相似
    def test_long_low(self):
        sc = simhash.simhash_check('test\org_long_low.txt','test\org_add_long_low.txt')  # noqa: E501
        result = sc.check()
        print('长文本低相似：',result)
        self.assertTrue(result<100 and result>0)
    #短文本高相似
    def test_short_high(self):
        sc = simhash.simhash_check('test\org_short_high.txt','test\org_add_short_high.txt')  # noqa: E501
        result = sc.check()
        print('短文本高相似：',result)
        self.assertTrue(result<100 and result>0)      
    #短文本低相似
    def test_short_low(self):
        sc = simhash.simhash_check('test\org_short_low.txt','test\org_add_short_low.txt')  # noqa: E501
        result = sc.check()
        print('短文本低相似：',result)
        self.assertTrue(result<100 and result>0)
if __name__ == '__main__':
    
    unittest.main()

