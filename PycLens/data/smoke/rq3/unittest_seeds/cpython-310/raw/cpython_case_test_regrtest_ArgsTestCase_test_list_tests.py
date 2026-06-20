# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ArgsTestCase_test_list_tests

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = [self.create_test() for i in range(5)]
    output = self.run_tests('--list-tests', *tests)
    self.assertEqual(output.rstrip().splitlines(), tests)
