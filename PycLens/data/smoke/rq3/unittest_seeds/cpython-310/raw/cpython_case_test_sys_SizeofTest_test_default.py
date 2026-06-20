# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SizeofTest_test_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    size = test.support.calcvobjsize
    self.assertEqual(sys.getsizeof(True), size('') + self.longdigit)
    self.assertEqual(sys.getsizeof(True, -1), size('') + self.longdigit)
