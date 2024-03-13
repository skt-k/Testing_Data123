# catandmouse/test_cat_mouse.py
import unittest
from Cat_Mouse.cat_mouse.py import cat_and_mouse

class TestCatAndMouse(unittest.TestCase):
    def test_cat_and_mouse_cat_a(self):
        result = cat_and_mouse(2, 5, 4)
        self.assertEqual(result, 'Cat B')

    def test_cat_and_mouse_cat_b(self):
        result = cat_and_mouse(7, 4, 6)
        self.assertEqual(result, 'Cat A')

    def test_cat_and_mouse_mouse_c(self):
        result = cat_and_mouse(3, 6, 5)
        self.assertEqual(result, 'Mouse C')

if __name__ == '__main__':
    unittest.main()
