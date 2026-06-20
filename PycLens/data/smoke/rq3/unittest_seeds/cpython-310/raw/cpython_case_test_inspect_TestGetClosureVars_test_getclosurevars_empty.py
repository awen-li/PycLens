# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetClosureVars_test_getclosurevars_empty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def foo():
        pass
    _empty = inspect.ClosureVars({}, {}, {}, set())
    self.assertEqual(inspect.getclosurevars(lambda : True), _empty)
    self.assertEqual(inspect.getclosurevars(foo), _empty)
