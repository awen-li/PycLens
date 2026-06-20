# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_constructor_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    size = MAX_Py_ssize_t
    self.assertRaises((OverflowError, MemoryError), self.type2test, size)
    try:
        bytearray(size - 4)
    except (OverflowError, MemoryError):
        pass
