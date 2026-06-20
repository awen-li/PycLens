# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TestRoundtrip_test_backslash_continuation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_roundtrip('x=1+\\\n1\n# This is a comment\\\n# This also\n')
    self.check_roundtrip('# Comment \\\nx = 0')
