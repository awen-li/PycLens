# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: LargeArrayTest_test_pop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    example = self.example(size)
    self.assertEqual(example.pop(0), 0)
    self.assertEqual(example[0], 1)
    self.assertEqual(example.pop(size + 1), 10)
    self.assertEqual(example[size + 1], 11)
    self.assertEqual(example.pop(1), 2)
    self.assertEqual(example[1], 3)
    self.assertEqual(len(example), size + 1)
    self.assertEqual(example.pop(), 11)
    self.assertEqual(len(example), size)
