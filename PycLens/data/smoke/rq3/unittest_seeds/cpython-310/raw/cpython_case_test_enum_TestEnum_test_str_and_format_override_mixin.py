# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_str_and_format_override_mixin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MixinWithStrFormatOverrides(float, Enum):
        one = 1.0
        two = 2.0

        def __str__(self):
            return 'Str!'

        def __format__(self, spec):
            return 'Format!'
    self.assertEqual(str(MixinWithStrFormatOverrides.one), 'Str!')
    self.assertEqual('{}'.format(MixinWithStrFormatOverrides.one), 'Format!')
