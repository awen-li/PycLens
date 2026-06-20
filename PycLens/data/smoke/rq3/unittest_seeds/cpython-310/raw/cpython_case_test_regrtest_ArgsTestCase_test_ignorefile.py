# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ArgsTestCase_test_ignorefile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import unittest\n\n            class Tests(unittest.TestCase):\n                def test_method1(self):\n                    pass\n                def test_method2(self):\n                    pass\n                def test_method3(self):\n                    pass\n                def test_method4(self):\n                    pass\n        ')
    all_methods = ['test_method1', 'test_method2', 'test_method3', 'test_method4']
    testname = self.create_test(code=code)
    filename = os_helper.TESTFN
    self.addCleanup(os_helper.unlink, filename)
    subset = ['test_method1', '%s.Tests.test_method3' % testname]
    with open(filename, 'w') as fp:
        for name in subset:
            print(name, file=fp)
    output = self.run_tests('-v', '--ignorefile', filename, testname)
    methods = self.parse_methods(output)
    subset = ['test_method2', 'test_method4']
    self.assertEqual(methods, subset)
