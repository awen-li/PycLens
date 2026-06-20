# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ArgsTestCase_test_findleaks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import _testcapi\n            import gc\n            import unittest\n\n            @_testcapi.with_tp_del\n            class Garbage:\n                def __tp_del__(self):\n                    pass\n\n            class Tests(unittest.TestCase):\n                def test_garbage(self):\n                    # create an uncollectable object\n                    obj = Garbage()\n                    obj.ref_cycle = obj\n                    obj = None\n        ')
    testname = self.create_test(code=code)
    output = self.run_tests('--fail-env-changed', testname, exitcode=3)
    self.check_executed_tests(output, [testname], env_changed=[testname], fail_env_changed=True)
    output = self.run_tests('--findleaks', testname, exitcode=3)
    self.check_executed_tests(output, [testname], env_changed=[testname], fail_env_changed=True)
