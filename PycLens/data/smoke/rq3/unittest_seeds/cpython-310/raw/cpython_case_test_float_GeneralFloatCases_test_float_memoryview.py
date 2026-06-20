# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: GeneralFloatCases_test_float_memoryview

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(float(memoryview(b'12.3')[1:4]), 2.3)
    self.assertEqual(float(memoryview(b'12.3\x00')[1:4]), 2.3)
    self.assertEqual(float(memoryview(b'12.3 ')[1:4]), 2.3)
    self.assertEqual(float(memoryview(b'12.3A')[1:4]), 2.3)
    self.assertEqual(float(memoryview(b'12.34')[1:4]), 2.3)
