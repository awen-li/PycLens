# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_str_and_format_override_enum

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class EnumWithStrFormatOverrides(Enum):
        one = auto()
        two = auto()

        def __str__(self):
            return 'Str!'

        def __format__(self, spec):
            return 'Format!'
    self.assertEqual(str(EnumWithStrFormatOverrides.one), 'Str!')
    self.assertEqual('{}'.format(EnumWithStrFormatOverrides.one), 'Format!')
