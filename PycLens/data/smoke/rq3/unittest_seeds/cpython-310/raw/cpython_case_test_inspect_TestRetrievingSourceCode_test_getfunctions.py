# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestRetrievingSourceCode_test_getfunctions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    functions = inspect.getmembers(mod, inspect.isfunction)
    self.assertEqual(functions, [('eggs', mod.eggs), ('lobbest', mod.lobbest), ('spam', mod.spam)])
