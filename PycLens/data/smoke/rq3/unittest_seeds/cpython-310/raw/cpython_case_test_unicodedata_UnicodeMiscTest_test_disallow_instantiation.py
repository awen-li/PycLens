# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicodedata.py
# case: UnicodeMiscTest_test_disallow_instantiation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    check_disallow_instantiation(self, unicodedata.UCD)
