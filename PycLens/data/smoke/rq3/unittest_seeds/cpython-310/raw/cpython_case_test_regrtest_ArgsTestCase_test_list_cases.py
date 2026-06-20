# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ArgsTestCase_test_list_cases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import unittest\n\n            class Tests(unittest.TestCase):\n                def test_method1(self):\n                    pass\n                def test_method2(self):\n                    pass\n        ')
    testname = self.create_test(code=code)
    all_methods = ['%s.Tests.test_method1' % testname, '%s.Tests.test_method2' % testname]
    output = self.run_tests('--list-cases', testname)
    self.assertEqual(output.splitlines(), all_methods)
    all_methods = ['%s.Tests.test_method1' % testname]
    output = self.run_tests('--list-cases', '-m', 'test_method1', testname)
    self.assertEqual(output.splitlines(), all_methods)
