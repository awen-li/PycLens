# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sort.py
# case: TestOptimizedCompares_test_unsafe_tuple_compare

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    check_against_PyObject_RichCompareBool(self, [float('nan')] * 100)
    check_against_PyObject_RichCompareBool(self, [float('nan') for _ in range(100)])
