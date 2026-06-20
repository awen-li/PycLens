# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_trace.py
# case: TestCoverage_test_coverage

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tracer = trace.Trace(trace=0, count=1)
    with captured_stdout() as stdout:
        self._coverage(tracer)
    stdout = stdout.getvalue()
    self.assertIn('pprint.py', stdout)
    self.assertIn('case.py', stdout)
    files = os.listdir(TESTFN)
    self.assertIn('pprint.cover', files)
    self.assertIn('unittest.case.cover', files)
