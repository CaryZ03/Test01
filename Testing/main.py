import unittest

from White import Triangle
from Black import CheckId


class MyTest(unittest.TestCase):
    # 编写测试用例，记得要以t开头，例：test
    # def testEqual(self):
    #     # 调用内部的测试方法，如：assertEqual,assertNotEqual 等
    #     self.assertEqual(Triangle.triangle(3, 4, 5), "regular triangle!")
    #
    # def testNotEqual(self):
    #     self.assertEqual(Triangle.triangle("3", 4, 5), "not a triangle!")

    def test1(self):
        self.assertEqual(CheckId.Black('110108202404260002').exec(), 1)
    def test2(self):
        self.assertEqual(CheckId.Black('110221201813010005').exec(), 1)
    def test3(self):
        self.assertEqual(CheckId.Black('110221201813010006').exec(), 1)
    def test4(self):
        self.assertEqual(CheckId.Black('110221201813010007').exec(), 1)

# 运行测试
if __name__ == '__main__':
    unittest.main()
