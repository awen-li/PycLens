# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetClosureVars_test_builtins_fallback

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (f, ns) = self._private_globals()
    ns.pop('__builtins__', None)
    expected = inspect.ClosureVars({}, {}, {'print': print}, {'path'})
    self.assertEqual(inspect.getclosurevars(f), expected)
