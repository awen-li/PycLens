# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_args_from_interpreter_flags

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for opts in ([], ['-B'], ['-s'], ['-S'], ['-E'], ['-v'], ['-b'], ['-q'], ['-I'], ['-bb'], ['-vvv'], ['-Wignore'], ['-X', 'dev'], ['-Wignore', '-X', 'dev'], ['-X', 'faulthandler'], ['-X', 'importtime'], ['-X', 'showrefcount'], ['-X', 'tracemalloc'], ['-X', 'tracemalloc=3']):
        with self.subTest(opts=opts):
            self.check_options(opts, 'args_from_interpreter_flags')
    self.check_options(['-I', '-E', '-s'], 'args_from_interpreter_flags', ['-I'])
