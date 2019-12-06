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

if __name__ == "__main__":
    unittest.main()
