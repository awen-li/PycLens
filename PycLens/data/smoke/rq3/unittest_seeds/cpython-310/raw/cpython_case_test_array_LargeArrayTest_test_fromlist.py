# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: LargeArrayTest_test_fromlist

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    example = self.example(size)
    example.fromlist([12, 13, 14, 15])
    self.assertEqual(len(example), size + 8)
    self.assertEqual(list(example[-8:]), [8, 9, 10, 11, 12, 13, 14, 15])
