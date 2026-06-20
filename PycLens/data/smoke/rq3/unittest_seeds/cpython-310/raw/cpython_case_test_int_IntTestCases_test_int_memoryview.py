# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_int.py
# case: IntTestCases_test_int_memoryview

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(int(memoryview(b'123')[1:3]), 23)
    self.assertEqual(int(memoryview(b'123\x00')[1:3]), 23)
    self.assertEqual(int(memoryview(b'123 ')[1:3]), 23)
    self.assertEqual(int(memoryview(b'123A')[1:3]), 23)
    self.assertEqual(int(memoryview(b'1234')[1:3]), 23)
