# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TestFrame_test_lazy_lines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    linecache.clearcache()
    f = traceback.FrameSummary('f', 1, 'dummy', lookup_line=False)
    self.assertEqual(None, f._line)
    linecache.lazycache('f', globals())
    self.assertEqual('"""Test cases for traceback module"""', f.line)
