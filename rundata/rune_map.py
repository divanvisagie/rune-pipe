from functools import partial


medeival_map = {
    'a': 'ᛆ',
    'b': 'ᛒ',
    'c': 'ᛌ',
    'd': 'ᛑ',
    'ð': 'ᚧ',
    'e': 'ᛂ',
    'f': 'ᚠ',
    'g': 'ᚵ',
    'G': 'ᚶ',
    'h': 'ᚼ',
    'i': 'ᛁ',
    'ï ': 'ᛇ',
    'k': 'ᚴ',
    'l': 'ᛚ',
    'L': 'ᛛ',
    'm': 'ᛘ',
    'n': 'ᚾ',
    'N': 'ᚿ',
    'o': 'ᚮ',
    'ô': 'ᚯ',  # Special case for Maeshowe, Orkney
    'p': 'ᛕ',  # in some cases this is ᛔ
    'r': 'ᚱ',
    'R': 'ᛦ',
    's': 'ᛋ',  # in norwegian this is ᛌ
    't': 'ᛏ',
    'þ': 'ᚦ',
    'u': 'ᚢ',
    'v': 'ᚡ',
    'y': 'ᚤ',  # in norwegian ᛦ
    'Y': 'ᚤ',
    'æ': 'ᛅ',
    'ø': 'ᚯ',  # third horizontal line on Maeshowe, Orkney
}

elder_map = {
    'a': 'ᚨ',
    'b': 'ᛒ',
    'c': 'ᚲ',
    'd': 'ᛞ',
    'e': 'ᛖ',
    'f': 'ᚠ',
    'g': 'ᚷ',
    'h': 'ᚺ',
    'i': 'ᛁ',
    'ï': 'ᛇ',
    'j': 'ᛃ',
    'k': 'ᚲ',
    'l': 'ᛚ',
    'L': 'ᛛ',
    'm': 'ᛗ',
    'ŋ': 'ᛜ',
    'n': 'ᚾ',
    'N': 'ᚿ',
    'o': 'ᛟ',
    'O': 'ᛟ',
    'p': 'ᛈ',
    'r': 'ᚱ',
    'R': 'ᛦ',
    's': 'ᛊ',
    't': 'ᛏ',
    'þ': 'ᚦ',
    'u': 'ᚢ',
    'w': 'ᚹ',
    'z': 'ᛉ',
}

viking_map = {
    'a': 'ᛅ',
    'b': 'ᛒ',
    'd': 'ᛑ',
    'ð': 'ᚧ',
    'e': 'ᛂ',
    'f': 'ᚠ',
    'g': 'ᚵ',
    'G': 'ᚶ',
    'h': 'ᚼ',
    'H': 'ᚺ',
    'i': 'ᛁ',
    'ï ': 'ᛇ',
    'k': 'ᚴ',
    'l': 'ᛚ',
    'L': 'ᛛ',
    'm': 'ᛘ',
    'n': 'ᚾ',
    'N': 'ᚿ',
    'o': 'ᚬ',
    'r': 'ᚱ',
    'R': 'ᛦ',
    's': 'ᛋ',
    't': 'ᛏ',
    'þ': 'ᚦ',
    'u': 'ᚢ',
    'y': 'ᚤ',  # in norwegian ᛦ
    'Y': 'ᚤ',
}


def de_transliterate(rune_map: dict[str, str], text):
    for t in text:
        if t in rune_map:
            text = text.replace(t, rune_map[t])
    return text


de_transliterate_viking = partial(de_transliterate, viking_map)
de_transliterate_elder = partial(de_transliterate, elder_map)
de_transliterate_medieval = partial(de_transliterate, medeival_map)
