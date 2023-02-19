import unittest
import logging
import os
import sys
sys.path.insert(1, os.getcwd())

from rundata.rune_map import de_transliterate_viking, de_transliterate_elder, de_transliterate_medieval  # noqa


class RuneMapTests(unittest.TestCase):

    def test_de_transliterate_viking(self):
        """ Test de_transliterate_viking() based on actual example from runestone U 124"""
        actual = de_transliterate_viking(
            "+ anutr + auk × þorkiRsl × þaiR × lRtu × rasa × stain × ifR + askaut +")
        expected = '+ ᛅᚾᚢᛏᚱ + ᛅᚢᚴ × ᚦᚬᚱᚴᛁᛦᛋᛚ × ᚦᛅᛁᛦ × ᛚᛦᛏᚢ × ᚱᛅᛋᛅ × ᛋᛏᛅᛁᚾ × ᛁᚠᛦ + ᛅᛋᚴᛅᚢᛏ +'
        self.assertEqual(actual, expected)

    def test_de_transliterate_proto_norse(self):
        """Test de_transliterate_proto_norse() based on actual example from runestone Ög 171 U	
        https://pub.raa.se/dokumentation/f2fd7196-e11a-440b-9531-5c626c6930b3/visning/1
        """
        actual = de_transliterate_elder("skiþaleubaz")
        expected = 'ᛊᚲᛁᚦᚨᛚᛖᚢᛒᚨᛉ'
        self.assertEqual(actual, expected)

    def test_de_transliterate_medieval(self):
        """Test de_transliterate_medieval() based on actual example from runestone Öl 53 M
        https://ia600904.us.archive.org/22/items/antiqvarisktidsk09kung/antiqvarisktidsk09kung.pdf
        https://www.arild-hauge.com/SRI/SRI-Oel-53-ALBOEKE-KYRKOGAARD.pdf
        """
        actual = de_transliterate_medieval(
            "þer liker æln")  # Note that this is not the full enscription but is the best documented part`
        expected = 'ᚦᛂᚱ ᛚᛁᚴᛂᚱ ᛅᛚᚾ'
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
    )
    unittest.main()
