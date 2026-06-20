# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TracebackCases_test_base_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = KeyboardInterrupt()
    lst = traceback.format_exception_only(e.__class__, e)
    self.assertEqual(lst, ['KeyboardInterrupt\n'])
