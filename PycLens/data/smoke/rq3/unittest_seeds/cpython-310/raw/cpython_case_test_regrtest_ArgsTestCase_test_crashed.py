# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ArgsTestCase_test_crashed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'import faulthandler; faulthandler._sigsegv()'
    crash_test = self.create_test(name='crash', code=code)
    tests = [crash_test]
    output = self.run_tests('-j2', *tests, exitcode=2)
    self.check_executed_tests(output, tests, failed=crash_test, randomize=True)
