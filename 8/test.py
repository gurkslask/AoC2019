import unittest
import main

class TestMain(unittest.TestCase):
    def test_2(self):
        print("test1")
        self.assertEqual(main.calc("123456789012", 3, 2, True), 1)
    def test_3(self):
        self.assertEqual(main.calc("123456189012", 3, 2, True), 1)
    def test_4(self):
        self.assertEqual(main.genimg(main.calc("0222112222120000", 2, 2, False), 2,2), [["0","1"],["1","0"]])

if __name__ == "__main__":
    unittest.main()
