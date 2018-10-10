import unittest

import pyramid_traversal_recursive
from pyramid_traversal_recursive import Pyramid


class TestSmallPyramid(unittest.TestCase):

    def setUp(self):
        pyramid_traversal_recursive.DEBUG = True
        self.pyramid = Pyramid.load_from_file('small_triangle.txt')

    def tearDown(self):
        pyramid_traversal_recursive.DEBUG = False

    def test_prettyPrintDebug(self):
        self.assertEqual(
            self.pyramid._pretty_pyramid,
            (
                '                    79\n'
                '                  82  04\n'
                '                86  93  64\n'
                '              34  30  17  44\n'
                '            41  79  83  33  86\n'
                '          10  34  55  92  26  23\n'
                '        54  84  30  79  40  30  65\n'
                '      94  64  79  36  79  78  72  36\n'
                '    12  88  25  57  72  37  37  45  26\n'
                '  92  24  07  07  04  48  25  60  54  72\n'
            )
        )
        # TODO assert print was called with pretty pyramid

    def test_linkedNodes(self):
        """
        Test that tree traversal works as expected, the correct values link together
        """
        # row 1, root
        self.assertEqual(self.pyramid.root.cost, 79)
        # row 2
        self.assertEqual(self.pyramid.root.left.cost, 82)
        self.assertEqual(self.pyramid.root.right.cost, 4)
        # row 3
        self.assertEqual(self.pyramid.root.left.left.cost, 86)
        self.assertEqual(
            self.pyramid.root.left.right.cost, self.pyramid.root.right.left.cost, 93
        )
        self.assertEqual(self.pyramid.root.right.right.cost, 64)

        # TODO rows 4 - 9

        # row 10 (some of it)
        self.assertEqual(  # bottom left
            self.pyramid.root.left.left.left.left.left.left.left.left.left.cost,
            92
        )

        self.assertEqual(  # bottom right
            self.pyramid.root.right.right.right.right.right.right.right.right.right.cost,
            72
        )

        # below the pyramid (some of it)
        self.assertEqual(
            self.pyramid.root.left.left.left.left.left.left.left.left.left.left,
            None
        )
        self.assertEqual(
            self.pyramid.root.right.right.right.right.right.right.right.right.right.right,
            None
        )

    def test_minPathSum(self):
        """
        79+04+64+17+33+26+30+72+37+25
        387
        """
        self.assertEqual(Pyramid.min_path_cost(self.pyramid.root), 387)


if __name__ == '__main__':
    unittest.main()
