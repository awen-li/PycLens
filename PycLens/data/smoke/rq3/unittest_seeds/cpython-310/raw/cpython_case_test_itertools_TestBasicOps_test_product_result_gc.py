# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_product_result_gc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    it = product([None, []])
    next(it)
    gc.collect()
    self.assertTrue(gc.is_tracked(next(it)))
