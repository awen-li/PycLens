# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ArgsTestCase_test_failing_test

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import unittest\n\n            class FailingTest(unittest.TestCase):\n                def test_failing(self):\n                    self.fail("bug")\n        ')
    test_ok = self.create_test('ok')
    test_failing = self.create_test('failing', code=code)
    tests = [test_ok, test_failing]
    output = self.run_tests(*tests, exitcode=2)
    self.check_executed_tests(output, tests, failed=test_failing)
