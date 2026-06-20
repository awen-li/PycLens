# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_repr_deep

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {}
    for i in range(sys.getrecursionlimit() + 100):
        d = {1: d}
    self.assertRaises(RecursionError, repr, d)
