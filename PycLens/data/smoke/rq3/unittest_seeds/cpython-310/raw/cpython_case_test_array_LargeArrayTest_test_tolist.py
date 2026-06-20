# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: LargeArrayTest_test_tolist

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    example = self.example(size)
    ls = example.tolist()
    self.assertEqual(len(ls), len(example))
    self.assertEqual(ls[:8], list(example[:8]))
    self.assertEqual(ls[-8:], list(example[-8:]))
