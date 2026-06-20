# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: TestInterpreterIsRunning_test_subinterpreter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    interp = interpreters.create()
    self.assertFalse(interp.is_running())
    with _running(interp):
        self.assertTrue(interp.is_running())
    self.assertFalse(interp.is_running())
