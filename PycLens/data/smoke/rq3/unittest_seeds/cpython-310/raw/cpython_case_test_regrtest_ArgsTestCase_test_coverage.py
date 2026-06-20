# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ArgsTestCase_test_coverage

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test = self.create_test('coverage')
    output = self.run_tests('--coverage', test)
    self.check_executed_tests(output, [test])
    regex = 'lines +cov% +module +\\(path\\)\\n(?: *[0-9]+ *[0-9]{1,2}% *[^ ]+ +\\([^)]+\\)+)+'
    self.check_line(output, regex)
