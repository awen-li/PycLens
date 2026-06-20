# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_trace.py
# case: TestFuncs_test_loop_caller_importing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.tracer.runfunc(traced_func_importing_caller, 1)
    expected = {self.filemod + ('traced_func_simple_caller',): 1, self.filemod + ('traced_func_linear',): 1, self.filemod + ('traced_func_importing_caller',): 1, self.filemod + ('traced_func_importing',): 1, (fix_ext_py(testmod.__file__), 'testmod', 'func'): 1}
    self.assertEqual(self.tracer.results().calledfuncs, expected)
