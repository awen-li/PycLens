# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_trace.py
# case: TestCoverage_test_coverage_ignore

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    libpath = os.path.normpath(os.path.dirname(os.__file__))
    tracer = trace.Trace(ignoredirs=[sys.base_prefix, sys.base_exec_prefix, libpath], trace=0, count=1)
    with captured_stdout() as stdout:
        self._coverage(tracer)
    if os.path.exists(TESTFN):
        files = os.listdir(TESTFN)
        self.assertEqual(files, ['_importlib.cover'])
