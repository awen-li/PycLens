# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: CommandLineTestCase_test_illegal_arguments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFailure('-z')
    self.assertFailure('spam')
    self.assertFailure('2004', 'spam')
    self.assertFailure('-t', 'html', '2004', '1')
