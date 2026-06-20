# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: GeneralFloatCases_test_floatconversion

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Foo1(object):

        def __float__(self):
            return 42.0

    class Foo2(float):

        def __float__(self):
            return 42.0

    class Foo3(float):

        def __new__(cls, value=0.0):
            return float.__new__(cls, 2 * value)

        def __float__(self):
            return self

    class Foo4(float):

        def __float__(self):
            return 42

    class FooStr(str):

        def __float__(self):
            return float(str(self)) + 1
    self.assertEqual(float(Foo1()), 42.0)
    self.assertEqual(float(Foo2()), 42.0)
    with self.assertWarns(DeprecationWarning):
        self.assertEqual(float(Foo3(21)), 42.0)
    self.assertRaises(TypeError, float, Foo4(42))
    self.assertEqual(float(FooStr('8')), 9.0)

    class Foo5:

        def __float__(self):
            return ''
    self.assertRaises(TypeError, time.sleep, Foo5())

    class F:

        def __float__(self):
            return OtherFloatSubclass(42.0)
    with self.assertWarns(DeprecationWarning):
        self.assertEqual(float(F()), 42.0)
    with self.assertWarns(DeprecationWarning):
        self.assertIs(type(float(F())), float)
    with self.assertWarns(DeprecationWarning):
        self.assertEqual(FloatSubclass(F()), 42.0)
    with self.assertWarns(DeprecationWarning):
        self.assertIs(type(FloatSubclass(F())), FloatSubclass)

    class MyIndex:

        def __init__(self, value):
            self.value = value

        def __index__(self):
            return self.value
    self.assertEqual(float(MyIndex(42)), 42.0)
    self.assertRaises(OverflowError, float, MyIndex(2 ** 2000))

    class MyInt:

        def __int__(self):
            return 42
    self.assertRaises(TypeError, float, MyInt())
