# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sort.py
# case: TestOptimizedCompares_test_safe_object_compare

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    heterogeneous_lists = [[0, 'foo'], [0.0, 'foo'], [('foo',), 'foo']]
    for L in heterogeneous_lists:
        self.assertRaises(TypeError, L.sort)
        self.assertRaises(TypeError, [(x,) for x in L].sort)
        self.assertRaises(TypeError, [((x,),) for x in L].sort)
    float_int_lists = [[1, 1.1], [1 << 70, 1.1], [1.1, 1], [1.1, 1 << 70]]
    for L in float_int_lists:
        check_against_PyObject_RichCompareBool(self, L)
