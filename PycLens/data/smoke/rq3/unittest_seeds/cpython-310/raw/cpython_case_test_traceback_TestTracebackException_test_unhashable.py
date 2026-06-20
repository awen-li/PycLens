# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TestTracebackException_test_unhashable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class UnhashableException(Exception):

        def __eq__(self, other):
            return True
    ex1 = UnhashableException('ex1')
    ex2 = UnhashableException('ex2')
    try:
        raise ex2 from ex1
    except UnhashableException:
        try:
            raise ex1
        except UnhashableException:
            exc_info = sys.exc_info()
    exc = traceback.TracebackException(*exc_info)
    formatted = list(exc.format())
    self.assertIn('UnhashableException: ex2\n', formatted[2])
    self.assertIn('UnhashableException: ex1\n', formatted[6])
