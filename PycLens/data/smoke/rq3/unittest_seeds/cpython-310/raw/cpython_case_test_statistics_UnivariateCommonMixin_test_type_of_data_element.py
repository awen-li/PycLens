# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: UnivariateCommonMixin_test_type_of_data_element

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyFloat(float):

        def __truediv__(self, other):
            return type(self)(super().__truediv__(other))

        def __add__(self, other):
            return type(self)(super().__add__(other))
        __radd__ = __add__
    raw = self.prepare_data()
    expected = self.func(raw)
    for kind in (float, MyFloat, Decimal, Fraction):
        data = [kind(x) for x in raw]
        result = type(expected)(self.func(data))
        self.assertEqual(result, expected)
