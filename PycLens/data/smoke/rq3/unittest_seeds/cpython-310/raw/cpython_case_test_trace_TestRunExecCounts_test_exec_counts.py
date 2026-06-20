# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_trace.py
# case: TestRunExecCounts_test_exec_counts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.tracer = Trace(count=1, trace=0, countfuncs=0, countcallers=0)
    code = 'traced_func_loop(2, 5)'
    code = compile(code, __file__, 'exec')
    self.tracer.runctx(code, globals(), vars())
    firstlineno = get_firstlineno(traced_func_loop)
    expected = {(self.my_py_filename, firstlineno + 1): 1, (self.my_py_filename, firstlineno + 2): 6, (self.my_py_filename, firstlineno + 3): 5, (self.my_py_filename, firstlineno + 4): 1}
    for k in expected.keys():
        self.assertEqual(self.tracer.results().counts[k], expected[k])
