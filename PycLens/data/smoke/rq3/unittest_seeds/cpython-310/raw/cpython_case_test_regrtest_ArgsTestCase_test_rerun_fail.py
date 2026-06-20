# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ArgsTestCase_test_rerun_fail

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import unittest\n\n            class Tests(unittest.TestCase):\n                def test_succeed(self):\n                    return\n\n                def test_fail_always(self):\n                    # test that always fails\n                    self.fail("bug")\n        ')
    testname = self.create_test(code=code)
    output = self.run_tests('-w', testname, exitcode=2)
    self.check_executed_tests(output, [testname], failed=testname, rerun={testname: 'test_fail_always'})
