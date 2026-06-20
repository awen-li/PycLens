# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlencode_Tests_test_nonstring_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual('a=1', urllib.parse.urlencode({'a': 1}))
    self.assertEqual('a=None', urllib.parse.urlencode({'a': None}))
