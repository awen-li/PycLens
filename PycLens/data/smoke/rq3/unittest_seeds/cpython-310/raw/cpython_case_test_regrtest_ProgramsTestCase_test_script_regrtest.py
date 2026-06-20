# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ProgramsTestCase_test_script_regrtest

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script = os.path.join(self.testdir, 'regrtest.py')
    args = [*self.python_args, script, *self.regrtest_args, *self.tests]
    self.run_tests(args)
