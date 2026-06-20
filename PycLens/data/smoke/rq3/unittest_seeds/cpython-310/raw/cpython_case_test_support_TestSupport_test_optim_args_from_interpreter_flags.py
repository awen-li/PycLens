# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_optim_args_from_interpreter_flags

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for opts in ([], ['-O'], ['-OO'], ['-OOOO']):
        with self.subTest(opts=opts):
            self.check_options(opts, 'optim_args_from_interpreter_flags')
