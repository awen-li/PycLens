# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ucn.py
# case: UnicodeNamesTest_test_ascii_letters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for char in ''.join(map(chr, range(ord('a'), ord('z')))):
        name = 'LATIN SMALL LETTER %s' % char.upper()
        code = unicodedata.lookup(name)
        self.assertEqual(unicodedata.name(code), name)
