# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_trace.py
# case: TestLineCounts_test_traced_func_linear

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = self.tracer.runfunc(traced_func_linear, 2, 5)
    self.assertEqual(result, 7)
    expected = {}
    firstlineno = get_firstlineno(traced_func_linear)
    for i in range(1, 5):
        expected[self.my_py_filename, firstlineno + i] = 1
    self.assertEqual(self.tracer.results().counts, expected)
