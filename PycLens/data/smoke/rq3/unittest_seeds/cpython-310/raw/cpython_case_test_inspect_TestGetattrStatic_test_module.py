# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetattrStatic_test_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sentinel = object()
    self.assertIsNot(inspect.getattr_static(sys, 'version', sentinel), sentinel)
