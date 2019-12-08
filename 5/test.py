import unittest
import main

class TestMain(unittest.TestCase):
    def test_2(self):
        self.assertEqual(main.calc("10101,2,1,0,99"), 4)
        self.assertEqual(main.calc("11101,4,4,0,99"), 8)
        self.assertEqual(main.calc("10001,2,1,0,99"), 3)
        self.assertEqual(main.calc("10002,2,1,0,99"), 2)
        self.assertEqual(main.calc("11102,8,5,0,99"), 40)

if __name__ == "__main__":
    unittest.main()
