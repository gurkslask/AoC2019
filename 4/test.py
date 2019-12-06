import unittest
import main

class TestMain(unittest.TestCase):
    def test_2(self):
        self.assertEqual(main.calc(111111), True)
        self.assertEqual(main.calc(223450), False)
        self.assertEqual(main.calc(123789), False)
        self.assertEqual(main.calcAdv(112233), True)
        self.assertEqual(main.calcAdv(123444), False)
        self.assertEqual(main.calcAdv(111122), True)
        self.assertEqual(main.calcAdv(221111), False)
        self.assertEqual(main.calcAdv(222111), False)
        self.assertEqual(main.calcAdv(222222), False)
        self.assertEqual(main.calcAdv(123456), False)
        self.assertEqual(main.calcAdv(123455), True)
        self.assertEqual(main.calcAdv(123555), False)
        self.assertEqual(main.calcAdv(112222), True)
        self.assertEqual(main.calcAdv(222222), False)
        self.assertEqual(main.calcAdv(222333), False)
        self.assertEqual(main.calcAdv(446665), False)

if __name__ == "__main__":
    unittest.main()
