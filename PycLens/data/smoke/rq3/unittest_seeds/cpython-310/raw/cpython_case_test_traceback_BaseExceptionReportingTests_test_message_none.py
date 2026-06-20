# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: BaseExceptionReportingTests_test_message_none

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    err = self.get_report(Exception(None))
    self.assertIn('Exception: None\n', err)
    err = self.get_report(Exception('None'))
    self.assertIn('Exception: None\n', err)
    err = self.get_report(Exception())
    self.assertIn('Exception\n', err)
    err = self.get_report(Exception(''))
    self.assertIn('Exception\n', err)
