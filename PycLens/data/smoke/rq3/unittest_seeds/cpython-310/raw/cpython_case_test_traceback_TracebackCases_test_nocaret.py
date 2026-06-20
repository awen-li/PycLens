# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TracebackCases_test_nocaret

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    exc = SyntaxError('error', ('x.py', 23, None, 'bad syntax'))
    err = traceback.format_exception_only(SyntaxError, exc)
    self.assertEqual(len(err), 3)
    self.assertEqual(err[1].strip(), 'bad syntax')
