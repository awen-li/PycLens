# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestInvalidArgumentConstructors_test_more_than_one_argument_actions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for action in ['store', 'append']:
        self.assertValueError('-x', nargs=0, action=action)
        self.assertValueError('spam', nargs=0, action=action)
        for nargs in [1, '*', '+']:
            self.assertValueError('-x', const='foo', nargs=nargs, action=action)
            self.assertValueError('spam', const='foo', nargs=nargs, action=action)
