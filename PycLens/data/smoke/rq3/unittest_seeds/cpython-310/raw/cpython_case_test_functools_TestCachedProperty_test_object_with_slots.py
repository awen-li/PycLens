# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestCachedProperty_test_object_with_slots

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    item = CachedCostItemWithSlots()
    with self.assertRaisesRegex(TypeError, "No '__dict__' attribute on 'CachedCostItemWithSlots' instance to cache 'cost' property."):
        item.cost
