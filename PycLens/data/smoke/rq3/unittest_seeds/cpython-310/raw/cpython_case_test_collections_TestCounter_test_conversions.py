# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCounter_test_conversions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = 'she sells sea shells by the sea shore'
    self.assertEqual(sorted(Counter(s).elements()), sorted(s))
    self.assertEqual(sorted(Counter(s)), sorted(set(s)))
    self.assertEqual(dict(Counter(s)), dict(Counter(s).items()))
    self.assertEqual(set(Counter(s)), set(s))
