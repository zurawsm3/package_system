import unittest

from main import Product


class TestCalc(unittest.TestCase):

    def test_return_col_box(self):
        p = Product("A", 3, 6, 9)
        self.assertEqual(p.return_col_box(0, 1, 0), 0, "Should be 0 col_boxes")
        self.assertEqual(p.return_col_box(0, 2, 0), 1, "Should be 1 col_box")
        self.assertEqual(p.return_col_box(0, 1, 3), 2, "Should be 2 col_boxes")

    def test_pack_order(self):
        p = Product("A", 3, 6, 9)
        self.assertDictEqual(p.pack_order(4), {'small_cardboard_box': 0, 'medium_cardboard_box': 1, 'large_cardboard_box': 0, 'collect_cardboard_box': 0})
        self.assertDictEqual(p.pack_order(12), {'small_cardboard_box': 0, 'medium_cardboard_box': 2, 'large_cardboard_box': 0, 'collect_cardboard_box': 1})
        self.assertDictEqual(p.pack_order(36), {'small_cardboard_box': 0, 'medium_cardboard_box': 0, 'large_cardboard_box': 4, 'collect_cardboard_box': 2})



if __name__ == '__main__':
    unittest.main()