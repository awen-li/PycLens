# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ArgsTestCase_test_slowest_interrupted

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = TEST_INTERRUPTED
    test = self.create_test('sigint', code=code)
    for multiprocessing in (False, True):
        with self.subTest(multiprocessing=multiprocessing):
            if multiprocessing:
                args = ('--slowest', '-j2', test)
            else:
                args = ('--slowest', test)
            output = self.run_tests(*args, exitcode=130)
            self.check_executed_tests(output, test, omitted=test, interrupted=True)
            regex = '10 slowest tests:\n'
            self.check_line(output, regex)
