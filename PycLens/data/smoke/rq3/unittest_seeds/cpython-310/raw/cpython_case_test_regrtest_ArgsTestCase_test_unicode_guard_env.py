# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: ArgsTestCase_test_unicode_guard_env

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    guard = os.environ.get(setup.UNICODE_GUARD_ENV)
    self.assertIsNotNone(guard, f'{setup.UNICODE_GUARD_ENV} not set')
    if guard.isascii():
        self.skipTest('Modified guard')
