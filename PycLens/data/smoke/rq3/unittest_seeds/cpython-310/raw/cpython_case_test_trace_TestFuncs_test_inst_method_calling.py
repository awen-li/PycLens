# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_trace.py
# case: TestFuncs_test_inst_method_calling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    obj = TracedClass(20)
    self.tracer.runfunc(obj.inst_method_calling, 1)
    expected = {self.filemod + ('TracedClass.inst_method_calling',): 1, self.filemod + ('TracedClass.inst_method_linear',): 1, self.filemod + ('traced_func_linear',): 1}
    self.assertEqual(self.tracer.results().calledfuncs, expected)
