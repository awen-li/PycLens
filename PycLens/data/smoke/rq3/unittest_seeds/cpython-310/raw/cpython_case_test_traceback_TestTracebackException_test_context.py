# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TestTracebackException_test_context

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        try:
            1 / 0
        finally:
            exc_info_context = sys.exc_info()
            exc_context = traceback.TracebackException(*exc_info_context)
            raise Exception('uh oh')
    except Exception:
        exc_info = sys.exc_info()
        exc = traceback.TracebackException(*exc_info)
        expected_stack = traceback.StackSummary.extract(traceback.walk_tb(exc_info[2]))
    self.assertEqual(None, exc.__cause__)
    self.assertEqual(exc_context, exc.__context__)
    self.assertEqual(False, exc.__suppress_context__)
    self.assertEqual(expected_stack, exc.stack)
    self.assertEqual(exc_info[0], exc.exc_type)
    self.assertEqual(str(exc_info[1]), str(exc))
