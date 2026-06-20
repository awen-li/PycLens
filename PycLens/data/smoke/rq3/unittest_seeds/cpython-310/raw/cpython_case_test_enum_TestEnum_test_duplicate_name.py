# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_duplicate_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):

        class Color(Enum):
            red = 1
            green = 2
            blue = 3
            red = 4
    with self.assertRaises(TypeError):

        class Color(Enum):
            red = 1
            green = 2
            blue = 3

            def red(self):
                return 'red'
    with self.assertRaises(TypeError):

        class Color(Enum):

            @property
            def red(self):
                return 'redder'
            red = 1
            green = 2
            blue = 3
