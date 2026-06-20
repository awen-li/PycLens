# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TestTracebackException_test_traceback_header

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    exc = traceback.TracebackException(Exception, Exception('haven'), None)
    self.assertEqual(list(exc.format()), ['Exception: haven\n'])
