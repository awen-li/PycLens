# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_funcattrs.py
# case: FunctionPropertiesTest_test_copying___code__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test():
        pass
    self.assertEqual(test(), None)
    test.__code__ = self.b.__code__
    self.assertEqual(test(), 3)
