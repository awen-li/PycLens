# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryview.py
# case: ArrayMemoryviewTest_test_array_assign

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array('i', range(10))
    m = memoryview(a)
    new_a = array.array('i', range(9, -1, -1))
    m[:] = new_a
    self.assertEqual(a, new_a)
