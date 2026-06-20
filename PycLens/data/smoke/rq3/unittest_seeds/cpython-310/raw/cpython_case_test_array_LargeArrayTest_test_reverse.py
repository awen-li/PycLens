# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: LargeArrayTest_test_reverse

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    example = self.example(size)
    example.reverse()
    self.assertEqual(len(example), size + 4)
    self.assertEqual(example[0], 11)
    self.assertEqual(example[3], 8)
    self.assertEqual(example[-1], 0)
    example.reverse()
    self.assertEqual(len(example), size + 4)
    self.assertEqual(list(example[:4]), [0, 1, 2, 3])
    self.assertEqual(list(example[-4:]), [8, 9, 10, 11])
