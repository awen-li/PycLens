# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorPickleTestCase_test_methodcaller

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    methodcaller = self.module.methodcaller

    class A:

        def foo(self, *args, **kwds):
            return args[0] + args[1]

        def bar(self, f=42):
            return f

        def baz(*args, **kwds):
            return (kwds['name'], kwds['self'])
    a = A()
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        with self.subTest(proto=proto):
            f = methodcaller('bar')
            f2 = self.copy(f, proto)
            self.assertEqual(repr(f2), repr(f))
            self.assertEqual(f2(a), f(a))
            f = methodcaller('foo', 1, 2)
            f2 = self.copy(f, proto)
            self.assertEqual(repr(f2), repr(f))
            self.assertEqual(f2(a), f(a))
            f = methodcaller('bar', f=5)
            f2 = self.copy(f, proto)
            self.assertEqual(repr(f2), repr(f))
            self.assertEqual(f2(a), f(a))
            f = methodcaller('baz', self='eggs', name='spam')
            f2 = self.copy(f, proto)
            self.assertEqual(f2(a), f(a))
