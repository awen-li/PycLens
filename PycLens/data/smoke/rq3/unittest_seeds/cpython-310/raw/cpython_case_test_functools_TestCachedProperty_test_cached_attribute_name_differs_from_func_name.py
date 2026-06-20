# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestCachedProperty_test_cached_attribute_name_differs_from_func_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    item = OptionallyCachedCostItem()
    self.assertEqual(item.get_cost(), 2)
    self.assertEqual(item.cached_cost, 3)
    self.assertEqual(item.get_cost(), 4)
    self.assertEqual(item.cached_cost, 3)
