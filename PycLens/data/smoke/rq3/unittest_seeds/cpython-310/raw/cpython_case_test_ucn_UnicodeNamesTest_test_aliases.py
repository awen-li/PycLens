# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ucn.py
# case: UnicodeNamesTest_test_aliases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    aliases = [('LATIN CAPITAL LETTER GHA', 418), ('LATIN SMALL LETTER GHA', 419), ('KANNADA LETTER LLLA', 3294), ('LAO LETTER FO FON', 3741), ('LAO LETTER FO FAY', 3743), ('LAO LETTER RO', 3747), ('LAO LETTER LO', 3749), ('TIBETAN MARK BKA- SHOG GI MGO RGYAN', 4048), ('YI SYLLABLE ITERATION MARK', 40981), ('PRESENTATION FORM FOR VERTICAL RIGHT WHITE LENTICULAR BRACKET', 65048), ('BYZANTINE MUSICAL SYMBOL FTHORA SKLIRON CHROMA VASIS', 118981)]
    for (alias, codepoint) in aliases:
        self.checkletter(alias, chr(codepoint))
        name = unicodedata.name(chr(codepoint))
        self.assertNotEqual(name, alias)
        self.assertEqual(unicodedata.lookup(alias), unicodedata.lookup(name))
        with self.assertRaises(KeyError):
            unicodedata.ucd_3_2_0.lookup(alias)
