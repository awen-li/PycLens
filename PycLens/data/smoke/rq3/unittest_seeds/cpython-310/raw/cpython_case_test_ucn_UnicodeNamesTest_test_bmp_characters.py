# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ucn.py
# case: UnicodeNamesTest_test_bmp_characters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for code in range(65536):
        char = chr(code)
        name = unicodedata.name(char, None)
        if name is not None:
            self.assertEqual(unicodedata.lookup(name), char)
