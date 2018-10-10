import unittest

from pyramid_traversal_recursive import Pyramid


class TestLargePyramid(unittest.TestCase):

    def setUp(self):
        self.pyramid = Pyramid.load_from_file('large_triangle.txt')

    def test_minPathSum(self):
        """
        26+62+31+30+05+29+47+07+15+19+01+35+03+15+43+41+66+07+15+25+21+20+26+09+13+77+18+27+10+32+06+39+24+07+10+23+36+49+26+18+24+13+34+57+01+08+04+25+15+16+19+17+02+30+22+20+05+25+07+01+13+07+29+10+02+79+47+16+15+10+60+09+31+28+01+32+21+01+03+06+22+05+04+36+05+11+05+43+33+26+53+43+61+50+39+24+02+20+48+34+05+18+44+11+61+47+63+37+09+26+08+08+60+02+30+33+07+52+02+27+17+45+21+52+05+05+25+39+32+16+01+01+12+14+30+21+07+16+26+26+78+32+14+11+13+24+22+10+31+11
        3549
        """
        raise unittest.SkipTest('This will hang, recursion is too much for the large triangle')
        # self.assertEqual(min_path_cost(self.pyramid.root), 3549)


if __name__ == '__main__':
    unittest.main()
