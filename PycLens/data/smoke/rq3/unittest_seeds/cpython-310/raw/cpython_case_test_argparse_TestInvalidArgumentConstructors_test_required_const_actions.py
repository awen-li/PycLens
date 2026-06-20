# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestInvalidArgumentConstructors_test_required_const_actions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for action in ['store_const', 'append_const']:
        self.assertTypeError('-x', nargs='+', action=action)
