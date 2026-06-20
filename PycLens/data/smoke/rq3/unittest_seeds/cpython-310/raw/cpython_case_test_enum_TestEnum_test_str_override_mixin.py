# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_str_override_mixin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MixinEnumWithStrOverride(float, Enum):
        one = 1.0
        two = 2.0

        def __str__(self):
            return 'Overridden!'
    self.assertEqual(str(MixinEnumWithStrOverride.one), 'Overridden!')
    self.assertEqual('{}'.format(MixinEnumWithStrOverride.one), 'Overridden!')
