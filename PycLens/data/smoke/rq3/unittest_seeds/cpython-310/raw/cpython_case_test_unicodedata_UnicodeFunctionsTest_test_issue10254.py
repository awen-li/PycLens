# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicodedata.py
# case: UnicodeFunctionsTest_test_issue10254

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = 'C̸' * 20 + 'Ç'
    b = 'C̸' * 20 + 'Ç'
    self.assertEqual(self.db.normalize('NFC', a), b)
