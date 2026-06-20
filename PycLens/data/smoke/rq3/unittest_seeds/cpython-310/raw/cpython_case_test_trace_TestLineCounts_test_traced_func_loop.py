# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_trace.py
# case: TestLineCounts_test_traced_func_loop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.tracer.runfunc(traced_func_loop, 2, 3)
    firstlineno = get_firstlineno(traced_func_loop)
    expected = {(self.my_py_filename, firstlineno + 1): 1, (self.my_py_filename, firstlineno + 2): 6, (self.my_py_filename, firstlineno + 3): 5, (self.my_py_filename, firstlineno + 4): 1}
    self.assertEqual(self.tracer.results().counts, expected)
