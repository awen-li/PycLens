# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TestTracebackException_test_no_refs_to_exception_and_traceback_objects

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        1 / 0
    except Exception:
        exc_info = sys.exc_info()
    refcnt1 = sys.getrefcount(exc_info[1])
    refcnt2 = sys.getrefcount(exc_info[2])
    exc = traceback.TracebackException(*exc_info)
    self.assertEqual(sys.getrefcount(exc_info[1]), refcnt1)
    self.assertEqual(sys.getrefcount(exc_info[2]), refcnt2)
