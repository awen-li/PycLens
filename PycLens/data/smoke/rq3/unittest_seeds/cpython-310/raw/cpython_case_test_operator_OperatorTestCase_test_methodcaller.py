# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorTestCase_test_methodcaller

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    operator = self.module
    self.assertRaises(TypeError, operator.methodcaller)
    self.assertRaises(TypeError, operator.methodcaller, 12)

    class A:

        def foo(self, *args, **kwds):
            return args[0] + args[1]

        def bar(self, f=42):
            return f

        def baz(*args, **kwds):
            return (kwds['name'], kwds['self'])
    a = A()
    f = operator.methodcaller('foo')
    self.assertRaises(IndexError, f, a)
    f = operator.methodcaller('foo', 1, 2)
    self.assertEqual(f(a), 3)
    self.assertRaises(TypeError, f)
    self.assertRaises(TypeError, f, a, 3)
    self.assertRaises(TypeError, f, a, spam=3)
    f = operator.methodcaller('bar')
    self.assertEqual(f(a), 42)
    self.assertRaises(TypeError, f, a, a)
    f = operator.methodcaller('bar', f=5)
    self.assertEqual(f(a), 5)
    f = operator.methodcaller('baz', name='spam', self='eggs')
    self.assertEqual(f(a), ('spam', 'eggs'))
