import unittest
from converter import convert, prompt

class ConverterTests(unittest.TestCase):
    def test_basic(self):
        self.assertIn("black_hair", convert("黑色頭髮的女孩"))
        self.assertIn("1girl", convert("黑色頭髮的女孩"))

    def test_no_duplicates(self):
        self.assertEqual(convert("女孩 girl"), ["1girl"])

    def test_empty(self):
        self.assertEqual(prompt(""), "")

    def test_english(self):
        self.assertIn("looking_at_viewer", convert("girl looking at viewer"))

if __name__ == "__main__":
    unittest.main()
