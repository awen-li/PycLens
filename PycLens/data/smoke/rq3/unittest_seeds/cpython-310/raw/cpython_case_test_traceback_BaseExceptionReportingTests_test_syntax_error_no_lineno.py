# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: BaseExceptionReportingTests_test_syntax_error_no_lineno

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = SyntaxError('bad syntax')
    msg = self.get_report(e).splitlines()
    self.assertEqual(msg, ['SyntaxError: bad syntax'])
    e.lineno = 100
    msg = self.get_report(e).splitlines()
    self.assertEqual(msg, ['  File "<string>", line 100', 'SyntaxError: bad syntax'])
    e = SyntaxError('bad syntax')
    e.filename = 'myfile.py'
    msg = self.get_report(e).splitlines()
    self.assertEqual(msg, ['SyntaxError: bad syntax (myfile.py)'])
    e.lineno = 100
    msg = self.get_report(e).splitlines()
    self.assertEqual(msg, ['  File "myfile.py", line 100', 'SyntaxError: bad syntax'])
