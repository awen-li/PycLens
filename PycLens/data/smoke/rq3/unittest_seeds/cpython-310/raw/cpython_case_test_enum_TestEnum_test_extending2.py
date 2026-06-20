# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_extending2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Shade(Enum):

        def shade(self):
            print(self.name)

    class Color(Shade):
        red = 1
        green = 2
        blue = 3
    with self.assertRaises(TypeError):

        class MoreColor(Color):
            cyan = 4
            magenta = 5
            yellow = 6
