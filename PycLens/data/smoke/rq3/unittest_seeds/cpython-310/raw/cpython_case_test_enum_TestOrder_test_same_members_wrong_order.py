# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestOrder_test_same_members_wrong_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaisesRegex(TypeError, 'member order does not match _order_'):

        class Color(Enum):
            _order_ = 'red green blue'
            red = 1
            blue = 3
            green = 2
