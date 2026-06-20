# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TestTracebackException_test_limit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def recurse(n):
        if n:
            recurse(n - 1)
        else:
            1 / 0
    try:
        recurse(10)
    except Exception:
        exc_info = sys.exc_info()
        exc = traceback.TracebackException(*exc_info, limit=5)
        expected_stack = traceback.StackSummary.extract(traceback.walk_tb(exc_info[2]), limit=5)
    self.assertEqual(expected_stack, exc.stack)
