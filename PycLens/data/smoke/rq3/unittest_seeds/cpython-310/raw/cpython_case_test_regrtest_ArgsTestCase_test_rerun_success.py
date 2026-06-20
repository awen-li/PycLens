# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ArgsTestCase_test_rerun_success

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import builtins\n            import unittest\n\n            class Tests(unittest.TestCase):\n                def test_succeed(self):\n                    return\n\n                def test_fail_once(self):\n                    if not hasattr(builtins, \'_test_failed\'):\n                        builtins._test_failed = True\n                        self.fail("bug")\n        ')
    testname = self.create_test(code=code)
    output = self.run_tests('-w', testname, exitcode=0)
    self.check_executed_tests(output, [testname], rerun={testname: 'test_fail_once'})
