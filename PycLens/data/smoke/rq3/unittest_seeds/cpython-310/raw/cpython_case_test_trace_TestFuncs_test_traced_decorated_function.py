# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_trace.py
# case: TestFuncs_test_traced_decorated_function

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.tracer.runfunc(traced_decorated_function)
    expected = {self.filemod + ('traced_decorated_function',): 1, self.filemod + ('decorator_fabric',): 1, self.filemod + ('decorator2',): 1, self.filemod + ('decorator1',): 1, self.filemod + ('func',): 1}
    self.assertEqual(self.tracer.results().calledfuncs, expected)
