# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: IsRunningTests_test_subinterpreter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    interp = interpreters.create()
    self.assertFalse(interpreters.is_running(interp))
    with _running(interp):
        self.assertTrue(interpreters.is_running(interp))
    self.assertFalse(interpreters.is_running(interp))
