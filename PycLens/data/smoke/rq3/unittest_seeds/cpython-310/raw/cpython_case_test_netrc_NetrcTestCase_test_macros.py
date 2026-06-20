# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_netrc.py
# case: NetrcTestCase_test_macros

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nrc = self.make_nrc('            macdef macro1\n            line1\n            line2\n\n            macdef macro2\n            line3\n            line4\n            ')
    self.assertEqual(nrc.macros, {'macro1': ['line1\n', 'line2\n'], 'macro2': ['line3\n', 'line4\n']})
