# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestBuggyCases_test_multiple_children_classes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertSourceEqual(mod2.cls203, 203, 209)
    self.assertSourceEqual(mod2.cls203.cls204, 204, 206)
    self.assertSourceEqual(mod2.cls203.cls204.cls205, 205, 206)
    self.assertSourceEqual(mod2.cls203.cls207, 207, 209)
    self.assertSourceEqual(mod2.cls203.cls207.cls205, 208, 209)
