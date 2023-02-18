""" Unit tests"""

import logging
import unittest

from functools import partial
from rundata_utils import extract_token_instances_from_text, has_same_repeated_character
logger = logging.getLogger(__name__)


class TestRundataUtils(unittest.TestCase):
    """ Unit tests for rundata_utils.py"""

    def test_get_rundata(self):
        """ Test get_rundata()"""
        actual = has_same_repeated_character("... ...")
        self.assertEqual(actual, True)
        actual = has_same_repeated_character("aaaa")
        self.assertEqual(actual, True)

    def test_token_instances_from_text(self):
        """ Test extract_token_instances_from_text()"""
        actual = extract_token_instances_from_text("test", "test test test")
        self.assertEqual(len(actual), 3)

    def test_partial_application(self):
        pf = partial(extract_token_instances_from_text, "test")
        actual = pf("test test test")
        self.assertEqual(len(actual), 3)


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
    unittest.main()
