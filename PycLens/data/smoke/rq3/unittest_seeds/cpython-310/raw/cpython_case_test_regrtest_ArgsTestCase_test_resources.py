# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ArgsTestCase_test_resources

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = {}
    for resource in ('audio', 'network'):
        code = textwrap.dedent('\n                        from test import support; support.requires(%r)\n                        import unittest\n                        class PassingTest(unittest.TestCase):\n                            def test_pass(self):\n                                pass\n                    ' % resource)
        tests[resource] = self.create_test(resource, code)
    test_names = sorted(tests.values())
    output = self.run_tests('-u', 'all', *test_names)
    self.check_executed_tests(output, test_names)
    output = self.run_tests('-uaudio', *test_names)
    self.check_executed_tests(output, test_names, skipped=tests['network'])
    output = self.run_tests(*test_names)
    self.check_executed_tests(output, test_names, skipped=test_names)
