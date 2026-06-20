# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_funcattrs.py
# case: StaticMethodAttrsTest_test_func_attribute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        pass
    c = classmethod(f)
    self.assertTrue(c.__func__ is f)
    s = staticmethod(f)
    self.assertTrue(s.__func__ is f)
