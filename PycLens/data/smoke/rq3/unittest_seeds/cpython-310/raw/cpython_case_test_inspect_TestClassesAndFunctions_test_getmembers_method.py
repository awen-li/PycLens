# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestClassesAndFunctions_test_getmembers_method

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class B:

        def f(self):
            pass
    self.assertIn(('f', B.f), inspect.getmembers(B))
    self.assertNotIn(('f', B.f), inspect.getmembers(B, inspect.ismethod))
    b = B()
    self.assertIn(('f', b.f), inspect.getmembers(b))
    self.assertIn(('f', b.f), inspect.getmembers(b, inspect.ismethod))
