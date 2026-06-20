# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_format_override_enum

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class EnumWithFormatOverride(Enum):
        one = 1.0
        two = 2.0

        def __format__(self, spec):
            return 'Format!!'
    self.assertEqual(str(EnumWithFormatOverride.one), 'EnumWithFormatOverride.one')
    self.assertEqual('{}'.format(EnumWithFormatOverride.one), 'Format!!')
