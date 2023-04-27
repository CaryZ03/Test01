import unittest

from White import Triangle
from Black import CheckId


class MyTest(unittest.TestCase):
    # 编写测试用例，记得要以t开头，例：test
    def testNotTriangle1(self):
        self.assertEqual(Triangle.triangle(3, 3, 3.5), "not a triangle!")

    def testNotTriangle2(self):
        self.assertEqual(Triangle.triangle(3, 3, 6), "not a triangle!")

    def testEquilateral(self):
        self.assertEqual(Triangle.triangle(3, 3, 3), "equilateral triangle!")

    def testIsosceles(self):
        self.assertEqual(Triangle.triangle(3, 3, 4), "isosceles triangle!")

    def testRegular(self):
        self.assertEqual(Triangle.triangle(3, 4, 5), "regular triangle!")

    # def test1(self):
    #     self.assertEqual(CheckId.Black('110108999904260007').exec(), 1)

# 运行测试
if __name__ == '__main__':
    unittest.main()
