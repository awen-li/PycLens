# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decimal.py
# case: ContextInputValidation_test_invalid_context

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Context = self.decimal.Context
    DefaultContext = self.decimal.DefaultContext
    c = DefaultContext.copy()
    for attr in ['prec', 'Emax']:
        setattr(c, attr, 999999)
        self.assertEqual(getattr(c, attr), 999999)
        self.assertRaises(ValueError, setattr, c, attr, -1)
        self.assertRaises(TypeError, setattr, c, attr, 'xyz')
    setattr(c, 'Emin', -999999)
    self.assertEqual(getattr(c, 'Emin'), -999999)
    self.assertRaises(ValueError, setattr, c, 'Emin', 1)
    self.assertRaises(TypeError, setattr, c, 'Emin', (1, 2, 3))
    self.assertRaises(TypeError, setattr, c, 'rounding', -1)
    self.assertRaises(TypeError, setattr, c, 'rounding', 9)
    self.assertRaises(TypeError, setattr, c, 'rounding', 1.0)
    self.assertRaises(TypeError, setattr, c, 'rounding', 'xyz')
    for attr in ['capitals', 'clamp']:
        self.assertRaises(ValueError, setattr, c, attr, -1)
        self.assertRaises(ValueError, setattr, c, attr, 2)
        self.assertRaises(TypeError, setattr, c, attr, [1, 2, 3])
    self.assertRaises(AttributeError, setattr, c, 'emax', 100)
    self.assertRaises(TypeError, setattr, c, 'flags', [])
    self.assertRaises(KeyError, setattr, c, 'flags', {})
    self.assertRaises(KeyError, setattr, c, 'traps', {'InvalidOperation': 0})
    for attr in ['prec', 'Emax', 'Emin', 'rounding', 'capitals', 'clamp', 'flags', 'traps']:
        self.assertRaises(AttributeError, c.__delattr__, attr)
    self.assertRaises(TypeError, getattr, c, 9)
    self.assertRaises(TypeError, setattr, c, 9)
    self.assertRaises(TypeError, Context, rounding=999999)
    self.assertRaises(TypeError, Context, rounding='xyz')
    self.assertRaises(ValueError, Context, clamp=2)
    self.assertRaises(ValueError, Context, capitals=-1)
    self.assertRaises(KeyError, Context, flags=['P'])
    self.assertRaises(KeyError, Context, traps=['Q'])
    self.assertRaises(TypeError, Context, flags=(0, 1))
    self.assertRaises(TypeError, Context, traps=(1, 0))
