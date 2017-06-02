import unittest

from create_box import create_box

first_box_expected = """
****
****
****
""".lstrip()

second_box_expected = """
@
""".lstrip()

third_box_expected = """
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
""".lstrip()

from create_box import create_box_border

first_box_border_expected = """
****
*  *
****
""".lstrip()

second_box_border_expected = """
@@@@@
@   @
@   @
@   @
@@@@@
""".lstrip()

third_box__border_expected = """
xxxxxxxxxxxxxxxxxxxxxxxx
x                      x
xxxxxxxxxxxxxxxxxxxxxxxx
""".lstrip()

class TestCreateBox(unittest.TestCase):
    def test_box(self):
        self.assertEqual(create_box(3, 4, '*'), first_box_expected)

    def test_small_box(self):
        self.assertEqual(create_box(1, 1, '@'), second_box_expected)

    def test_large_box(self):
        self.assertEqual(create_box(3, 24, 'x'), third_box_expected)

class TestCreateBoxBorder(unittest.TestCase):
    def test_box_border(self):
        self.assertEqual(create_box_border(3, 4, '*'), first_box_border_expected)

    def test_medium_box_border(self):
        self.assertEqual(create_box_border(5, 5, '@'), second_box_border_expected)

    def test_large_box_border(self):
        self.assertEqual(create_box_border(3, 24, 'x'), third_box__border_expected)
