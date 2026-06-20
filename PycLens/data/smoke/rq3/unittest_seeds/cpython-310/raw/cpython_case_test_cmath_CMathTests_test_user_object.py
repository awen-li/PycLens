# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmath.py
# case: CMathTests_test_user_object

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cx_arg = 4.419414439 + 1.497100113j
    flt_arg = -6.131677725
    non_complexes = ['not complex', 1, 5, 2.0, None, object(), NotImplemented]

    class MyComplex(object):

        def __init__(self, value):
            self.value = value

        def __complex__(self):
            return self.value

    class MyComplexOS:

        def __init__(self, value):
            self.value = value

        def __complex__(self):
            return self.value

    class SomeException(Exception):
        pass

    class MyComplexException(object):

        def __complex__(self):
            raise SomeException

    class MyComplexExceptionOS:

        def __complex__(self):
            raise SomeException

    class NeitherComplexNorFloat(object):
        pass

    class NeitherComplexNorFloatOS:
        pass

    class Index:

        def __int__(self):
            return 2

        def __index__(self):
            return 2

    class MyInt:

        def __int__(self):
            return 2

    class FloatAndComplex(object):

        def __float__(self):
            return flt_arg

        def __complex__(self):
            return cx_arg

    class FloatAndComplexOS:

        def __float__(self):
            return flt_arg

        def __complex__(self):
            return cx_arg

    class JustFloat(object):

        def __float__(self):
            return flt_arg

    class JustFloatOS:

        def __float__(self):
            return flt_arg
    for f in self.test_functions:
        self.assertEqual(f(MyComplex(cx_arg)), f(cx_arg))
        self.assertEqual(f(MyComplexOS(cx_arg)), f(cx_arg))
        self.assertEqual(f(FloatAndComplex()), f(cx_arg))
        self.assertEqual(f(FloatAndComplexOS()), f(cx_arg))
        self.assertEqual(f(JustFloat()), f(flt_arg))
        self.assertEqual(f(JustFloatOS()), f(flt_arg))
        self.assertEqual(f(Index()), f(int(Index())))
        self.assertRaises(TypeError, f, NeitherComplexNorFloat())
        self.assertRaises(TypeError, f, MyInt())
        self.assertRaises(Exception, f, NeitherComplexNorFloatOS())
        for bad_complex in non_complexes:
            self.assertRaises(TypeError, f, MyComplex(bad_complex))
            self.assertRaises(TypeError, f, MyComplexOS(bad_complex))
        self.assertRaises(SomeException, f, MyComplexException())
        self.assertRaises(SomeException, f, MyComplexExceptionOS())
