# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: LargeArrayTest_test_remove

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    example = self.example(size)
    example.remove(0)
    self.assertEqual(len(example), size + 3)
    self.assertEqual(example[0], 1)
    example.remove(10)
    self.assertEqual(len(example), size + 2)
    self.assertEqual(example[size], 9)
    self.assertEqual(example[size + 1], 11)
