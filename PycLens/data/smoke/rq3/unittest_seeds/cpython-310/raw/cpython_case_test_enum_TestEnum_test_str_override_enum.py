# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_str_override_enum

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class EnumWithStrOverrides(Enum):
        one = auto()
        two = auto()

        def __str__(self):
            return 'Str!'
    self.assertEqual(str(EnumWithStrOverrides.one), 'Str!')
    self.assertEqual('{}'.format(EnumWithStrOverrides.one), 'Str!')
