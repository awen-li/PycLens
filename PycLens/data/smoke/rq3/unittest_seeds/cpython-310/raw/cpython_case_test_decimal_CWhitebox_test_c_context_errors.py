# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: CWhitebox_test_c_context_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Context = C.Context
    InvalidOperation = C.InvalidOperation
    Overflow = C.Overflow
    FloatOperation = C.FloatOperation
    localcontext = C.localcontext
    getcontext = C.getcontext
    setcontext = C.setcontext
    HAVE_CONFIG_64 = C.MAX_PREC > 425000000
    c = Context()
    self.assertRaises(KeyError, c.flags.__setitem__, 801, 0)
    self.assertRaises(KeyError, c.traps.__setitem__, 801, 0)
    self.assertRaises(ValueError, c.flags.__delitem__, Overflow)
    self.assertRaises(ValueError, c.traps.__delitem__, InvalidOperation)
    self.assertRaises(TypeError, setattr, c, 'flags', ['x'])
    self.assertRaises(TypeError, setattr, c, 'traps', ['y'])
    self.assertRaises(KeyError, setattr, c, 'flags', {0: 1})
    self.assertRaises(KeyError, setattr, c, 'traps', {0: 1})
    d = c.flags.copy()
    del d[FloatOperation]
    d['XYZ'] = 91283719
    self.assertRaises(KeyError, setattr, c, 'flags', d)
    self.assertRaises(KeyError, setattr, c, 'traps', d)
    int_max = 2 ** 63 - 1 if HAVE_CONFIG_64 else 2 ** 31 - 1
    gt_max_emax = 10 ** 18 if HAVE_CONFIG_64 else 10 ** 9
    for attr in ['prec', 'Emax']:
        self.assertRaises(ValueError, setattr, c, attr, gt_max_emax)
    self.assertRaises(ValueError, setattr, c, 'Emin', -gt_max_emax)
    self.assertRaises(ValueError, Context, prec=gt_max_emax)
    self.assertRaises(ValueError, Context, Emax=gt_max_emax)
    self.assertRaises(ValueError, Context, Emin=-gt_max_emax)
    self.assertRaises(OverflowError, Context, prec=int_max + 1)
    self.assertRaises(OverflowError, Context, Emax=int_max + 1)
    self.assertRaises(OverflowError, Context, Emin=-int_max - 2)
    self.assertRaises(OverflowError, Context, clamp=int_max + 1)
    self.assertRaises(OverflowError, Context, capitals=int_max + 1)
    for attr in ('prec', 'Emin', 'Emax', 'capitals', 'clamp'):
        self.assertRaises(OverflowError, setattr, c, attr, int_max + 1)
        self.assertRaises(OverflowError, setattr, c, attr, -int_max - 2)
        if sys.platform != 'win32':
            self.assertRaises(ValueError, setattr, c, attr, int_max)
            self.assertRaises(ValueError, setattr, c, attr, -int_max - 1)
    if C.MAX_PREC == 425000000:
        self.assertRaises(OverflowError, getattr(c, '_unsafe_setprec'), int_max + 1)
        self.assertRaises(OverflowError, getattr(c, '_unsafe_setemax'), int_max + 1)
        self.assertRaises(OverflowError, getattr(c, '_unsafe_setemin'), -int_max - 2)
    if C.MAX_PREC == 425000000:
        self.assertRaises(ValueError, getattr(c, '_unsafe_setprec'), 0)
        self.assertRaises(ValueError, getattr(c, '_unsafe_setprec'), 1070000001)
        self.assertRaises(ValueError, getattr(c, '_unsafe_setemax'), -1)
        self.assertRaises(ValueError, getattr(c, '_unsafe_setemax'), 1070000001)
        self.assertRaises(ValueError, getattr(c, '_unsafe_setemin'), -1070000001)
        self.assertRaises(ValueError, getattr(c, '_unsafe_setemin'), 1)
    for attr in ['capitals', 'clamp']:
        self.assertRaises(ValueError, setattr, c, attr, -1)
        self.assertRaises(ValueError, setattr, c, attr, 2)
        self.assertRaises(TypeError, setattr, c, attr, [1, 2, 3])
        if HAVE_CONFIG_64:
            self.assertRaises(ValueError, setattr, c, attr, 2 ** 32)
            self.assertRaises(ValueError, setattr, c, attr, 2 ** 32 + 1)
    self.assertRaises(TypeError, exec, 'with localcontext("xyz"): pass', locals())
    self.assertRaises(TypeError, exec, 'with localcontext(context=getcontext()): pass', locals())
    saved_context = getcontext()
    self.assertRaises(TypeError, setcontext, 'xyz')
    setcontext(saved_context)
