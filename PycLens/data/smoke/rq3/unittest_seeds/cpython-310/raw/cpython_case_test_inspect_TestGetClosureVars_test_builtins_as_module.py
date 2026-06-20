# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetClosureVars_test_builtins_as_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (f, ns) = self._private_globals()
    ns['__builtins__'] = os
    expected = inspect.ClosureVars({}, {}, {'path': os.path}, {'print'})
    self.assertEqual(inspect.getclosurevars(f), expected)
