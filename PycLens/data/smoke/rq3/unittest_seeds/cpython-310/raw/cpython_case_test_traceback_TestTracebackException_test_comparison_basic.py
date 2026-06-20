# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TestTracebackException_test_comparison_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        1 / 0
    except Exception:
        exc_info = sys.exc_info()
        exc = traceback.TracebackException(*exc_info)
        exc2 = traceback.TracebackException(*exc_info)
    self.assertIsNot(exc, exc2)
    self.assertEqual(exc, exc2)
    self.assertNotEqual(exc, object())
    self.assertEqual(exc, ALWAYS_EQ)
