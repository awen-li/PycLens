# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetClosureVars_test_getclosurevars_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class T:
        pass
    self.assertRaises(TypeError, inspect.getclosurevars, 1)
    self.assertRaises(TypeError, inspect.getclosurevars, list)
    self.assertRaises(TypeError, inspect.getclosurevars, {})
