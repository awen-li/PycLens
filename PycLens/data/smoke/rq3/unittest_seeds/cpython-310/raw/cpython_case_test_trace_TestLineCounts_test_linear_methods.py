# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_trace.py
# case: TestLineCounts_test_linear_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for methname in ['inst_method_linear']:
        tracer = Trace(count=1, trace=0, countfuncs=0, countcallers=0)
        traced_obj = TracedClass(25)
        method = getattr(traced_obj, methname)
        tracer.runfunc(method, 20)
        firstlineno = get_firstlineno(method)
        expected = {(self.my_py_filename, firstlineno + 1): 1}
        self.assertEqual(tracer.results().counts, expected)
