# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_trace.py
# case: TestLineCounts_test_trace_list_comprehension

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.tracer.runfunc(traced_caller_list_comprehension)
    firstlineno_calling = get_firstlineno(traced_caller_list_comprehension)
    firstlineno_called = get_firstlineno(traced_doubler)
    expected = {(self.my_py_filename, firstlineno_calling + 1): 1, (self.my_py_filename, firstlineno_calling + 2): 12, (self.my_py_filename, firstlineno_calling + 3): 1, (self.my_py_filename, firstlineno_called + 1): 10}
    self.assertEqual(self.tracer.results().counts, expected)
