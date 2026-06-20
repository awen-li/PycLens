# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestPredicates_test_isclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.istest(inspect.isclass, 'mod.StupidGit')
    self.assertTrue(inspect.isclass(list))

    class CustomGetattr(object):

        def __getattr__(self, attr):
            return None
    self.assertFalse(inspect.isclass(CustomGetattr()))
