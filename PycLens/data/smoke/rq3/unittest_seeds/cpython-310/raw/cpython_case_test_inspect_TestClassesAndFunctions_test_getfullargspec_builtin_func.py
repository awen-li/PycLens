# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestClassesAndFunctions_test_getfullargspec_builtin_func

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _testcapi
    builtin = _testcapi.docstring_with_signature_with_defaults
    spec = inspect.getfullargspec(builtin)
    self.assertEqual(spec.defaults[0], 'avocado')
