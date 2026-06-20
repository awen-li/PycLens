# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestOrder_test_order_has_extra_members_with_aliases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaisesRegex(TypeError, 'member order does not match _order_'):

        class Color(Enum):
            _order_ = 'red green blue purple'
            red = 1
            green = 2
            blue = 3
            verde = green
