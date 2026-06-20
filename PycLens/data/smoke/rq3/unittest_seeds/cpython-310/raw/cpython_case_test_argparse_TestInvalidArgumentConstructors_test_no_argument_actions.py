# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestInvalidArgumentConstructors_test_no_argument_actions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for action in ['store_const', 'store_true', 'store_false', 'append_const', 'count']:
        for attrs in [dict(type=int), dict(nargs='+'), dict(choices='ab')]:
            self.assertTypeError('-x', action=action, **attrs)
