# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: CWhitebox_test_va_args_exceptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Decimal = C.Decimal
    Context = C.Context
    x = Decimal('10001111111')
    for attr in ['exp', 'is_normal', 'is_subnormal', 'ln', 'log10', 'logb', 'logical_invert', 'next_minus', 'next_plus', 'normalize', 'number_class', 'sqrt', 'to_eng_string']:
        func = getattr(x, attr)
        self.assertRaises(TypeError, func, context='x')
        self.assertRaises(TypeError, func, 'x', context=None)
    for attr in ['compare', 'compare_signal', 'logical_and', 'logical_or', 'max', 'max_mag', 'min', 'min_mag', 'remainder_near', 'rotate', 'scaleb', 'shift']:
        func = getattr(x, attr)
        self.assertRaises(TypeError, func, context='x')
        self.assertRaises(TypeError, func, 'x', context=None)
    self.assertRaises(TypeError, x.to_integral, rounding=None, context=[])
    self.assertRaises(TypeError, x.to_integral, rounding={}, context=[])
    self.assertRaises(TypeError, x.to_integral, [], [])
    self.assertRaises(TypeError, x.to_integral_value, rounding=None, context=[])
    self.assertRaises(TypeError, x.to_integral_value, rounding={}, context=[])
    self.assertRaises(TypeError, x.to_integral_value, [], [])
    self.assertRaises(TypeError, x.to_integral_exact, rounding=None, context=[])
    self.assertRaises(TypeError, x.to_integral_exact, rounding={}, context=[])
    self.assertRaises(TypeError, x.to_integral_exact, [], [])
    self.assertRaises(TypeError, x.fma, 1, 2, context='x')
    self.assertRaises(TypeError, x.fma, 1, 2, 'x', context=None)
    self.assertRaises(TypeError, x.quantize, 1, [], context=None)
    self.assertRaises(TypeError, x.quantize, 1, [], rounding=None)
    self.assertRaises(TypeError, x.quantize, 1, [], [])
    c = Context()
    self.assertRaises(TypeError, c.power, 1, 2, mod='x')
    self.assertRaises(TypeError, c.power, 1, 'x', mod=None)
    self.assertRaises(TypeError, c.power, 'x', 2, mod=None)
