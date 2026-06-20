# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_unhandled

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for exc_type in (ValueError, BrokenStrException):
        with self.subTest(exc_type):
            try:
                exc = exc_type('test message')
                raise exc
            except exc_type:
                with captured_stderr() as stderr:
                    sys.__excepthook__(*sys.exc_info())
            report = stderr.getvalue()
            self.assertIn('test_exceptions.py', report)
            self.assertIn('raise exc', report)
            self.assertIn(exc_type.__name__, report)
            if exc_type is BrokenStrException:
                self.assertIn('<exception str() failed>', report)
            else:
                self.assertIn('test message', report)
            self.assertTrue(report.endswith('\n'))
