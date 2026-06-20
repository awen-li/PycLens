# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TestTracebackException_test_from_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def foo():
        1 / 0
    try:
        foo()
    except Exception as e:
        exc_info = sys.exc_info()
        self.expected_stack = traceback.StackSummary.extract(traceback.walk_tb(exc_info[2]), limit=1, lookup_lines=False, capture_locals=True)
        self.exc = traceback.TracebackException.from_exception(e, limit=1, lookup_lines=False, capture_locals=True)
    expected_stack = self.expected_stack
    exc = self.exc
    self.assertEqual(None, exc.__cause__)
    self.assertEqual(None, exc.__context__)
    self.assertEqual(False, exc.__suppress_context__)
    self.assertEqual(expected_stack, exc.stack)
    self.assertEqual(exc_info[0], exc.exc_type)
    self.assertEqual(str(exc_info[1]), str(exc))
