# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_trace.py
# case: TestLineCounts_test_traced_decorated_function

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.tracer.runfunc(traced_decorated_function)
    firstlineno = get_firstlineno(traced_decorated_function)
    expected = {(self.my_py_filename, firstlineno + 1): 1, (self.my_py_filename, firstlineno + 2): 1, (self.my_py_filename, firstlineno + 3): 1, (self.my_py_filename, firstlineno + 4): 1, (self.my_py_filename, firstlineno + 5): 1, (self.my_py_filename, firstlineno + 6): 1, (self.my_py_filename, firstlineno + 7): 1, (self.my_py_filename, firstlineno + 8): 1, (self.my_py_filename, firstlineno + 9): 1, (self.my_py_filename, firstlineno + 10): 1, (self.my_py_filename, firstlineno + 11): 1}
    self.assertEqual(self.tracer.results().counts, expected)
