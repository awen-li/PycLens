# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: NumberTest_test_iterationcontains

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode, range(10))
    self.assertEqual(list(a), list(range(10)))
    b = array.array(self.typecode, [20])
    self.assertEqual(a[-1] in a, True)
    self.assertEqual(b[0] not in a, True)
