# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_list.py
# case: ListTest_test_len

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    super().test_len()
    self.assertEqual(len([]), 0)
    self.assertEqual(len([0]), 1)
    self.assertEqual(len([0, 1, 2]), 3)
