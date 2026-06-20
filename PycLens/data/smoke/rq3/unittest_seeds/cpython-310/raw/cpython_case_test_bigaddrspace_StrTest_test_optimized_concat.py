# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigaddrspace.py
# case: StrTest_test_optimized_concat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        x = 'x' * int(MAX_Py_ssize_t // (1.1 * self.unicodesize))
        with self.assertRaises(MemoryError) as cm:
            x = x + x
        with self.assertRaises(MemoryError) as cm:
            x += x
    finally:
        x = None
