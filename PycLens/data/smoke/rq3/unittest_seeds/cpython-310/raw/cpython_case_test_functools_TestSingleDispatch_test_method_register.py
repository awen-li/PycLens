# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestSingleDispatch_test_method_register

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:

        @functools.singledispatchmethod
        def t(self, arg):
            self.arg = 'base'

        @t.register(int)
        def _(self, arg):
            self.arg = 'int'

        @t.register(str)
        def _(self, arg):
            self.arg = 'str'
    a = A()
    a.t(0)
    self.assertEqual(a.arg, 'int')
    aa = A()
    self.assertFalse(hasattr(aa, 'arg'))
    a.t('')
    self.assertEqual(a.arg, 'str')
    aa = A()
    self.assertFalse(hasattr(aa, 'arg'))
    a.t(0.0)
    self.assertEqual(a.arg, 'base')
    aa = A()
    self.assertFalse(hasattr(aa, 'arg'))
