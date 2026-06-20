# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_trace.py
# case: TestLineCounts_test_traced_func_importing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.tracer.runfunc(traced_func_importing, 2, 5)
    firstlineno = get_firstlineno(traced_func_importing)
    expected = {(self.my_py_filename, firstlineno + 1): 1, (fix_ext_py(testmod.__file__), 2): 1, (fix_ext_py(testmod.__file__), 3): 1}
    self.assertEqual(self.tracer.results().counts, expected)
