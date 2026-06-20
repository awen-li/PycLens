# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestInvalidArgumentConstructors_test_missing_destination

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTypeError()
    for action in ['append', 'store']:
        self.assertTypeError(action=action)
