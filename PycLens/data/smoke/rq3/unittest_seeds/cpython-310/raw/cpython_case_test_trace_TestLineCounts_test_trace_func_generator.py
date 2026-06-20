# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_trace.py
# case: TestLineCounts_test_trace_func_generator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.tracer.runfunc(traced_func_calling_generator)
    firstlineno_calling = get_firstlineno(traced_func_calling_generator)
    firstlineno_gen = get_firstlineno(traced_func_generator)
    expected = {(self.my_py_filename, firstlineno_calling + 1): 1, (self.my_py_filename, firstlineno_calling + 2): 11, (self.my_py_filename, firstlineno_calling + 3): 10, (self.my_py_filename, firstlineno_gen + 1): 1, (self.my_py_filename, firstlineno_gen + 2): 11, (self.my_py_filename, firstlineno_gen + 3): 10}
    self.assertEqual(self.tracer.results().counts, expected)
