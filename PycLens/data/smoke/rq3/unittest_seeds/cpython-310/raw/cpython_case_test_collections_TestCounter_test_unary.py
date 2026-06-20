# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCounter_test_unary

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = Counter(a=-5, b=0, c=5, d=10, e=15, g=40)
    self.assertEqual(dict(+c), dict(c=5, d=10, e=15, g=40))
    self.assertEqual(dict(-c), dict(a=5))
