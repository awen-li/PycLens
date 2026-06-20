# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: CBytesIOTest_test_cow_mutable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ba = bytearray(1024)
    old_rc = sys.getrefcount(ba)
    memio = self.ioclass(ba)
    self.assertEqual(sys.getrefcount(ba), old_rc)
