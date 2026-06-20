# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: CWhitebox_test_c_context_errors_extra

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Context = C.Context
    InvalidOperation = C.InvalidOperation
    Overflow = C.Overflow
    localcontext = C.localcontext
    getcontext = C.getcontext
    setcontext = C.setcontext
    HAVE_CONFIG_64 = C.MAX_PREC > 425000000
    c = Context()
    int_max = 2 ** 63 - 1 if HAVE_CONFIG_64 else 2 ** 31 - 1
    self.assertRaises(OverflowError, setattr, c, '_allcr', int_max + 1)
    self.assertRaises(OverflowError, setattr, c, '_allcr', -int_max - 2)
    if sys.platform != 'win32':
        self.assertRaises(ValueError, setattr, c, '_allcr', int_max)
        self.assertRaises(ValueError, setattr, c, '_allcr', -int_max - 1)
    for attr in ('_flags', '_traps'):
        self.assertRaises(OverflowError, setattr, c, attr, int_max + 1)
        self.assertRaises(OverflowError, setattr, c, attr, -int_max - 2)
        if sys.platform != 'win32':
            self.assertRaises(TypeError, setattr, c, attr, int_max)
            self.assertRaises(TypeError, setattr, c, attr, -int_max - 1)
    self.assertRaises(ValueError, setattr, c, '_allcr', -1)
    self.assertRaises(ValueError, setattr, c, '_allcr', 2)
    self.assertRaises(TypeError, setattr, c, '_allcr', [1, 2, 3])
    if HAVE_CONFIG_64:
        self.assertRaises(ValueError, setattr, c, '_allcr', 2 ** 32)
        self.assertRaises(ValueError, setattr, c, '_allcr', 2 ** 32 + 1)
    for attr in ['_flags', '_traps']:
        self.assertRaises(TypeError, setattr, c, attr, 999999)
        self.assertRaises(TypeError, setattr, c, attr, 'x')
