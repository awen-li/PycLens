# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ArgsTestCase_test_no_tests_ran_skip

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import unittest\n\n            class Tests(unittest.TestCase):\n                def test_skipped(self):\n                    self.skipTest("because")\n        ')
    testname = self.create_test(code=code)
    output = self.run_tests(testname, exitcode=0)
    self.check_executed_tests(output, [testname])
