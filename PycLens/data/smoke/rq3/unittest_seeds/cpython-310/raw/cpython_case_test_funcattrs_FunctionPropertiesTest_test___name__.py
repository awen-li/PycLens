# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_funcattrs.py
# case: FunctionPropertiesTest_test___name__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.b.__name__, 'b')
    self.b.__name__ = 'c'
    self.assertEqual(self.b.__name__, 'c')
    self.b.__name__ = 'd'
    self.assertEqual(self.b.__name__, 'd')
    self.cannot_set_attr(self.b, '__name__', 7, TypeError)
    s = 'def f(): pass\nf.__name__'
    exec(s, {'__builtins__': {}})
    self.assertEqual(self.fi.a.__name__, 'a')
    self.cannot_set_attr(self.fi.a, '__name__', 'a', AttributeError)
