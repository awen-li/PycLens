# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dictviews.py
# case: DictSetTest_test_recursive_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {}
    d[42] = d.values()
    r = repr(d)
    self.assertIsInstance(r, str)
    d[42] = d.items()
    r = repr(d)
    self.assertIsInstance(r, str)
