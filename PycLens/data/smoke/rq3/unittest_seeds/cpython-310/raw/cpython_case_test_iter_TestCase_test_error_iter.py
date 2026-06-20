# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_error_iter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for typ in (DefaultIterClass, NoIterClass):
        self.assertRaises(TypeError, iter, typ())
    self.assertRaises(ZeroDivisionError, iter, BadIterableClass())
