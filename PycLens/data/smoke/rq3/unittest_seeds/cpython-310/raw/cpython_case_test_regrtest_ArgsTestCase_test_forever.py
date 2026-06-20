# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ArgsTestCase_test_forever

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import builtins\n            import unittest\n\n            class ForeverTester(unittest.TestCase):\n                def test_run(self):\n                    # Store the state in the builtins module, because the test\n                    # module is reload at each run\n                    if \'RUN\' in builtins.__dict__:\n                        builtins.__dict__[\'RUN\'] += 1\n                        if builtins.__dict__[\'RUN\'] >= 3:\n                            self.fail("fail at the 3rd runs")\n                    else:\n                        builtins.__dict__[\'RUN\'] = 1\n        ')
    test = self.create_test('forever', code=code)
    output = self.run_tests('--forever', test, exitcode=2)
    self.check_executed_tests(output, [test] * 3, failed=test)
