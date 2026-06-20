# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ArgsTestCase_test_slowest

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = [self.create_test() for index in range(3)]
    output = self.run_tests('--slowest', *tests)
    self.check_executed_tests(output, tests)
    regex = '10 slowest tests:\n(?:- %s: .*\n){%s}' % (self.TESTNAME_REGEX, len(tests))
    self.check_line(output, regex)
