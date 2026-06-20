# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestBuggyCases_test_nested_class_definition_inside_function

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertSourceEqual(mod2.func212(), 213, 214)
    self.assertSourceEqual(mod2.cls213, 218, 222)
    self.assertSourceEqual(mod2.cls213().func219(), 220, 221)
