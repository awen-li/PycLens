# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryview.py
# case: OtherTest_test_memoryview_hex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = b'0' * 200000
    m1 = memoryview(x)
    m2 = m1[::-1]
    self.assertEqual(m2.hex(), '30' * 200000)
