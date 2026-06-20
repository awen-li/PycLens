# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_new_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Color(Enum):
        red = 1
        green = 2
        blue = 3

        def __repr__(self):
            return "don't you just love shades of %s?" % self.name
    self.assertEqual(repr(Color.blue), "don't you just love shades of blue?")
