import unittest
import logging
import os
import sys
sys.path.insert(1, os.getcwd())

from rundata.rune_map import de_transliterate_viking  # noqa


class RuneMapTests(unittest.TestCase):

    def test_de_transliterate_viking(self):
        """ Test de_transliterate_viking() based on actual example from runestone U 124"""
        actual = de_transliterate_viking(
            "+ anutr + auk × þorkiRsl × þaiR × lRtu × rasa × stain × ifR + askaut +")
        expected = '+ ᛅᚾᚢᛏᚱ + ᛅᚢᚴ × ᚦᚬᚱᚴᛁᛦᛋᛚ × ᚦᛅᛁᛦ × ᛚᛦᛏᚢ × ᚱᛅᛋᛅ × ᛋᛏᛅᛁᚾ × ᛁᚠᛦ + ᛅᛋᚴᛅᚢᛏ +'
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
    )
    unittest.main()
