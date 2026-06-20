# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ArgsTestCase_test_no_test_ran_some_test_exist_some_not

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import unittest\n\n            class Tests(unittest.TestCase):\n                def test_bug(self):\n                    pass\n        ')
    testname = self.create_test(code=code)
    other_code = textwrap.dedent('\n            import unittest\n\n            class Tests(unittest.TestCase):\n                def test_other_bug(self):\n                    pass\n        ')
    testname2 = self.create_test(code=other_code)
    output = self.run_tests(testname, testname2, '-m', 'nosuchtest', '-m', 'test_other_bug', exitcode=0)
    self.check_executed_tests(output, [testname, testname2], no_test_ran=[testname])
