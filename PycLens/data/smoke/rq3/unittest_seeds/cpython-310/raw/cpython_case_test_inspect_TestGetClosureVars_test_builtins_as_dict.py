# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetClosureVars_test_builtins_as_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (f, ns) = self._private_globals()
    ns['__builtins__'] = {'path': 1}
    expected = inspect.ClosureVars({}, {}, {'path': 1}, {'print'})
    self.assertEqual(inspect.getclosurevars(f), expected)
