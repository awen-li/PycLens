# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hmac.py
# case: ConstructorTestCase_test_internal_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    check_disallow_instantiation(self, C_HMAC)
    with self.assertRaisesRegex(TypeError, 'immutable type'):
        C_HMAC.value = None
