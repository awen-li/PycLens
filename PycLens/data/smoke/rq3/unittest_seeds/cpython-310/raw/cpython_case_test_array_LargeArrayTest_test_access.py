# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: LargeArrayTest_test_access

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    example = self.example(size)
    self.assertEqual(example[0], 0)
    self.assertEqual(example[-(size + 4)], 0)
    self.assertEqual(example[size], 8)
    self.assertEqual(example[-4], 8)
    self.assertEqual(example[size + 3], 11)
    self.assertEqual(example[-1], 11)
