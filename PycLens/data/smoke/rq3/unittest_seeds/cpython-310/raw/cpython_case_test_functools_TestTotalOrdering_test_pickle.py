# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestTotalOrdering_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        for name in ('__lt__', '__gt__', '__le__', '__ge__'):
            with self.subTest(method=name, proto=proto):
                method = getattr(Orderable_LT, name)
                method_copy = pickle.loads(pickle.dumps(method, proto))
                self.assertIs(method_copy, method)
