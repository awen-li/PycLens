# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicodedata.py
# case: UnicodeMiscTest_test_bug_5828

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual('ᵹ'.lower(), 'ᵹ')
    self.assertEqual([c for c in range(sys.maxunicode + 1) if '\x00' in chr(c).lower() + chr(c).upper() + chr(c).title()], [0])
