# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_trace.py
# case: TestCallers_test_loop_caller_importing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.tracer.runfunc(traced_func_importing_caller, 1)
    expected = {((os.path.splitext(trace.__file__)[0] + '.py', 'trace', 'Trace.runfunc'), self.filemod + ('traced_func_importing_caller',)): 1, (self.filemod + ('traced_func_simple_caller',), self.filemod + ('traced_func_linear',)): 1, (self.filemod + ('traced_func_importing_caller',), self.filemod + ('traced_func_simple_caller',)): 1, (self.filemod + ('traced_func_importing_caller',), self.filemod + ('traced_func_importing',)): 1, (self.filemod + ('traced_func_importing',), (fix_ext_py(testmod.__file__), 'testmod', 'func')): 1}
    self.assertEqual(self.tracer.results().callers, expected)
