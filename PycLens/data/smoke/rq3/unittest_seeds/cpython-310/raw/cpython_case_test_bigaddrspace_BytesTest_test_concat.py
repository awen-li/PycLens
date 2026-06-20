# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigaddrspace.py
# case: BytesTest_test_concat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        x = b'x' * (MAX_Py_ssize_t - 128)
        self.assertRaises(OverflowError, operator.add, x, b'x' * 128)
    finally:
        x = None
