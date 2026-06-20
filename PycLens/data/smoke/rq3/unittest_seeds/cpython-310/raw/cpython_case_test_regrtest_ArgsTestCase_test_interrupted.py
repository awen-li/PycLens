# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ArgsTestCase_test_interrupted

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = TEST_INTERRUPTED
    test = self.create_test('sigint', code=code)
    output = self.run_tests(test, exitcode=130)
    self.check_executed_tests(output, test, omitted=test, interrupted=True)
