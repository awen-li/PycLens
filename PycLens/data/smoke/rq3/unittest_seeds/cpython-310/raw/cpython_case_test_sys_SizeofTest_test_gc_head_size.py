# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SizeofTest_test_gc_head_size

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    vsize = test.support.calcvobjsize
    gc_header_size = self.gc_headsize
    self.assertEqual(sys.getsizeof(True), vsize('') + self.longdigit)
    self.assertEqual(sys.getsizeof([]), vsize('Pn') + gc_header_size)
