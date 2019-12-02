import unittest
import main

class TestMain(unittest.TestCase):
    def test_2(self):
        self.assertEqual(main.calcAdv(1969), 966)
        self.assertEqual(main.calcAdv(100756), 50346)

if __name__ == "__main__":
    unittest.main()
