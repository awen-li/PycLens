# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: CheckActualTests_test_finds_expected_number_of_tests

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    args = ['-Wd', '-E', '-bb', '-m', 'test.regrtest', '--list-tests']
    output = self.run_python(args)
    rough_number_of_tests_found = len(output.splitlines())
    actual_testsuite_glob = os.path.join(glob.escape(os.path.dirname(__file__)), 'test*.py')
    rough_counted_test_py_files = len(glob.glob(actual_testsuite_glob))
    self.assertGreater(rough_number_of_tests_found, rough_counted_test_py_files * 9 // 10, msg=f"Unexpectedly low number of tests found in:\n{', '.join(output.splitlines())}")
