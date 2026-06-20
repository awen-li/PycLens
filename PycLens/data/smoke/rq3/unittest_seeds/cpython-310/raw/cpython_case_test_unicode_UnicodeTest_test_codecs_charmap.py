# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_codecs_charmap

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = bytes(range(128))
    for encoding in ('cp037', 'cp1026', 'cp273', 'cp437', 'cp500', 'cp720', 'cp737', 'cp775', 'cp850', 'cp852', 'cp855', 'cp858', 'cp860', 'cp861', 'cp862', 'cp863', 'cp865', 'cp866', 'cp1125', 'iso8859_10', 'iso8859_13', 'iso8859_14', 'iso8859_15', 'iso8859_2', 'iso8859_3', 'iso8859_4', 'iso8859_5', 'iso8859_6', 'iso8859_7', 'iso8859_9', 'koi8_r', 'koi8_t', 'koi8_u', 'kz1048', 'latin_1', 'mac_cyrillic', 'mac_latin2', 'cp1250', 'cp1251', 'cp1252', 'cp1253', 'cp1254', 'cp1255', 'cp1256', 'cp1257', 'cp1258', 'cp856', 'cp857', 'cp864', 'cp869', 'cp874', 'mac_greek', 'mac_iceland', 'mac_roman', 'mac_turkish', 'cp1006', 'iso8859_8'):
        self.assertEqual(str(s, encoding).encode(encoding), s)
    s = bytes(range(128, 256))
    for encoding in ('cp037', 'cp1026', 'cp273', 'cp437', 'cp500', 'cp720', 'cp737', 'cp775', 'cp850', 'cp852', 'cp855', 'cp858', 'cp860', 'cp861', 'cp862', 'cp863', 'cp865', 'cp866', 'cp1125', 'iso8859_10', 'iso8859_13', 'iso8859_14', 'iso8859_15', 'iso8859_2', 'iso8859_4', 'iso8859_5', 'iso8859_9', 'koi8_r', 'koi8_u', 'latin_1', 'mac_cyrillic', 'mac_latin2'):
        self.assertEqual(str(s, encoding).encode(encoding), s)
