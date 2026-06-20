# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: TestInterpreterAttrs_test_subinterpreter_isolated_explicit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    interp1 = interpreters.create(isolated=True)
    interp2 = interpreters.create(isolated=False)
    self.assertTrue(interp1.isolated)
    self.assertFalse(interp2.isolated)
