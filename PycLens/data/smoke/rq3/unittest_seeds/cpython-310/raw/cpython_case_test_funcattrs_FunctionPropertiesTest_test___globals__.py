# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_funcattrs.py
# case: FunctionPropertiesTest_test___globals__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIs(self.b.__globals__, globals())
    self.cannot_set_attr(self.b, '__globals__', 2, (AttributeError, TypeError))
