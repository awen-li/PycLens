# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigaddrspace.py
# case: BytesTest_test_optimized_concat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        x = b'x' * (MAX_Py_ssize_t - 128)
        with self.assertRaises(OverflowError) as cm:
            x = x + b'x' * 128
        with self.assertRaises(OverflowError) as cm:
            x += b'x' * 128
    finally:
        x = None
