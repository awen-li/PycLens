# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicodedata.py
# case: UnicodeFunctionsTest_test_name_inverse_lookup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in range(sys.maxunicode + 1):
        char = chr(i)
        if (looked_name := self.db.name(char, None)):
            self.assertEqual(self.db.lookup(looked_name), char)
