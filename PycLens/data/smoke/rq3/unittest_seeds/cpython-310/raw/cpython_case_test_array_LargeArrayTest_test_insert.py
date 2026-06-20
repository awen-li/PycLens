# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: LargeArrayTest_test_insert

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    example = self.example(size)
    example.insert(0, 12)
    example.insert(10, 13)
    example.insert(size + 1, 14)
    self.assertEqual(len(example), size + 7)
    self.assertEqual(example[0], 12)
    self.assertEqual(example[10], 13)
    self.assertEqual(example[size + 1], 14)
