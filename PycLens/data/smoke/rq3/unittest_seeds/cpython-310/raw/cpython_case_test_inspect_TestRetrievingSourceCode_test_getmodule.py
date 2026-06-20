# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestRetrievingSourceCode_test_getmodule

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(inspect.getmodule(mod), mod)
    self.assertEqual(inspect.getmodule(mod.StupidGit), mod)
    self.assertEqual(inspect.getmodule(mod.StupidGit.abuse), mod)
    self.assertEqual(inspect.getmodule(mod.StupidGit.abuse), mod)
    self.assertEqual(inspect.getmodule(str), sys.modules['builtins'])
    self.assertEqual(inspect.getmodule(None, modfile), mod)
