# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ArgsTestCase_test_env_changed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import unittest\n\n            class Tests(unittest.TestCase):\n                def test_env_changed(self):\n                    open("env_changed", "w").close()\n        ')
    testname = self.create_test(code=code)
    output = self.run_tests(testname)
    self.check_executed_tests(output, [testname], env_changed=testname)
    output = self.run_tests('--fail-env-changed', testname, exitcode=3)
    self.check_executed_tests(output, [testname], env_changed=testname, fail_env_changed=True)
