# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_auto_name_inherit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class AutoNameEnum(Enum):

        def _generate_next_value_(name, start, count, last):
            return name

    class Color(AutoNameEnum):
        red = auto()
        blue = auto()
        green = auto()
    self.assertEqual(list(Color), [Color.red, Color.blue, Color.green])
    self.assertEqual(Color.red.value, 'red')
    self.assertEqual(Color.blue.value, 'blue')
    self.assertEqual(Color.green.value, 'green')
