# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestInvalidArgumentConstructors_test_no_argument_no_const_actions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for action in ['store_true', 'store_false', 'count']:
        self.assertTypeError('-x', const='foo', action=action)
        self.assertTypeError('-x', nargs='*', action=action)
