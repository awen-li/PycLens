# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TracebackFormatTests_test_unhashable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import exception_print

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
            (exc_type, exc_val, exc_tb) = sys.exc_info()
    with captured_output('stderr') as stderr_f:
        exception_print(exc_val)
    tb = stderr_f.getvalue().strip().splitlines()
    self.assertEqual(11, len(tb))
    self.assertEqual(context_message.strip(), tb[5])
    self.assertIn('UnhashableException: ex2', tb[3])
    self.assertIn('UnhashableException: ex1', tb[10])
