import unittest
import sys
import os

sys.path.append(os.path.dirname(sys.path[0]))
import simhash  # noqa: E402

class Testsimhash(unittest.TestCase):
    #空文本
    def test_empty(self): 
        sc = simhash.simhash_check('D:\git\Sundaland\\202121331073\\test\org_empty.txt','D:\git\Sundaland\\202121331073\\test\org_add_empty.txt')  # noqa: E501
        result = sc.check()
        print('空文本:',result)
        self.assertEqual(result,1)
    #长文本、相似度高
    def test_long_high(self):
        sc = simhash.simhash_check('D:\git\Sundaland\\202121331073\\test\org_long_high.txt','D:\git\Sundaland\\202121331073\\test\org_add_long_high.txt')  # noqa: E501
        result = sc.check()
        print('长文本高相似：',result)
        self.assertTrue(result<=1 and result>=0)
    #长文本低相似
    def test_long_low(self):
        sc = simhash.simhash_check('D:\git\Sundaland\\202121331073\\test\org_long_low.txt','D:\git\Sundaland\\202121331073\\test\org_add_long_low.txt')  # noqa: E501
        result = sc.check()
        print('长文本低相似：',result)
        self.assertTrue(result<=1 and result>=0)
    #短文本高相似
    def test_short_high(self):
        sc = simhash.simhash_check('D:\git\Sundaland\\202121331073\\test\org_short_high.txt','D:\git\Sundaland\\202121331073\\test\org_add_short_high.txt')  # noqa: E501
        result = sc.check()
        print('短文本高相似：',result)
        self.assertTrue(result<=1 and result>=0)      
    #短文本低相似
    def test_short_low(self):
        sc = simhash.simhash_check('D:\git\Sundaland\\202121331073\\test\org_short_low.txt','D:\git\Sundaland\\202121331073\\test\org_add_short_low.txt')  # noqa: E501
        result = sc.check()
        print('短文本低相似：',result)
        self.assertTrue(result<=1 and result>=0)
    #中英文
    def test_cn_en(self):
        sc = simhash.simhash_check('D:\git\Sundaland\\202121331073\\test\org_cn.txt','D:\git\Sundaland\\202121331073\\test\org_en.txt')  # noqa: E501
        result = sc.check()
        print('中英文：',result)
        self.assertTrue(result<=1 and result>=0)
    #常规1
    def test_normal1(self):
        sc = simhash.simhash_check('D:\git\Sundaland\\202121331073\\test\org_normal1.txt','D:\git\Sundaland\\202121331073\\test\org_add_normal1.txt')  # noqa: E501
        result = sc.check()
        print('常规1：',result)
        self.assertTrue(result<=1 and result>=0)
    #常规2
    def test_normal2(self):
        sc = simhash.simhash_check('D:\git\Sundaland\\202121331073\\test\org_normal2.txt','D:\git\Sundaland\\202121331073\\test\org_add_normal2.txt')  # noqa: E501
        result = sc.check()
        print('常规2：',result)
        self.assertTrue(result<=1 and result>=0)
    #常规3
    def test_normal3(self):
        sc = simhash.simhash_check('D:\git\Sundaland\\202121331073\\test\org_normal3.txt','D:\git\Sundaland\\202121331073\\test\org_add_normal3.txt')  # noqa: E501
        result = sc.check()
        print('常规3：',result)
        self.assertTrue(result<=1 and result>=0)
    #常规4
    def test_normal4(self):
        sc = simhash.simhash_check('D:\git\Sundaland\\202121331073\\test\org_normal4.txt','D:\git\Sundaland\\202121331073\\test\org_add_normal4.txt')  # noqa: E501
        result = sc.check()
        print('常规4：',result)
        self.assertTrue(result<=1 and result>=0)
    #异常1
    def test_error1(self):
        os.system('python D:\git\Sundaland\\202121331073\main.py')
    #异常2
    def test_error2(self):
        os.system('python D:\git\Sundaland\\202121331073\main.py org.txt org_add.txt ans')   # noqa: E501


if __name__ == '__main__':
    unittest.main()

