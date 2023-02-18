""" Unit tests"""

import unittest

from rundata_utils import has_same_repeated_character


class TestRundataUtils(unittest.TestCase):
    """ Unit tests for rundata_utils.py"""

    def test_get_rundata(self):
        """ Test get_rundata()"""
        actual = has_same_repeated_character("... ...")
        self.assertEqual(actual, True)
        actual = has_same_repeated_character("aaaa")
        self.assertEqual(actual, True)


if __name__ == '__main__':
    unittest.main()
