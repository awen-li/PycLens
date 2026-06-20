# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_product_issue_25021

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = product((1, 2), (3,))
    p.__setstate__((0, 4096))
    self.assertEqual(next(p), (2, 3))
    p = product((1, 2), (), (3,))
    p.__setstate__((0, 0, 4096))
    self.assertRaises(StopIteration, next, p)
