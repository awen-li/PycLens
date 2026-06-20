# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_enum_with_value_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Huh(Enum):
        name = 1
        value = 2
    self.assertEqual(list(Huh), [Huh.name, Huh.value])
    self.assertIs(type(Huh.name), Huh)
    self.assertEqual(Huh.name.name, 'name')
    self.assertEqual(Huh.name.value, 1)
