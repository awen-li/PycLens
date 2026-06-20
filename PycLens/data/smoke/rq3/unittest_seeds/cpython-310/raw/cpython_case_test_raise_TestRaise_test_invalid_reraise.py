# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_raise.py
# case: TestRaise_test_invalid_reraise

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        raise
    except RuntimeError as e:
        self.assertIn('No active exception', str(e))
    else:
        self.fail('No exception raised')
