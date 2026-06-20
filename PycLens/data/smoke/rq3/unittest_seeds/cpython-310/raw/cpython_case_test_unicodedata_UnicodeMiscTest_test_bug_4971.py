# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicodedata.py
# case: UnicodeMiscTest_test_bug_4971

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual('Ǆ'.title(), 'ǅ')
    self.assertEqual('ǅ'.title(), 'ǅ')
    self.assertEqual('ǆ'.title(), 'ǅ')
