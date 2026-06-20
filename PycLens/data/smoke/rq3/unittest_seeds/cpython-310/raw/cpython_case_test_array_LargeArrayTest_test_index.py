# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: LargeArrayTest_test_index

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    example = self.example(size)
    self.assertEqual(example.index(0), 0)
    self.assertEqual(example.index(1), 1)
    self.assertEqual(example.index(7), 7)
    self.assertEqual(example.index(11), size + 3)
