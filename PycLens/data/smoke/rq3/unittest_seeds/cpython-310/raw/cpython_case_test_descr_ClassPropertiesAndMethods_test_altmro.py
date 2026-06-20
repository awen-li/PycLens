# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_altmro

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(object):

        def f(self):
            return 'A'

    class B(A):
        pass

    class C(A):

        def f(self):
            return 'C'

    class D(B, C):
        pass
    self.assertEqual(A.mro(), [A, object])
    self.assertEqual(A.__mro__, (A, object))
    self.assertEqual(B.mro(), [B, A, object])
    self.assertEqual(B.__mro__, (B, A, object))
    self.assertEqual(C.mro(), [C, A, object])
    self.assertEqual(C.__mro__, (C, A, object))
    self.assertEqual(D.mro(), [D, B, C, A, object])
    self.assertEqual(D.__mro__, (D, B, C, A, object))
    self.assertEqual(D().f(), 'C')

    class PerverseMetaType(type):

        def mro(cls):
            L = type.mro(cls)
            L.reverse()
            return L

    class X(D, B, C, A, metaclass=PerverseMetaType):
        pass
    self.assertEqual(X.__mro__, (object, A, C, B, D, X))
    self.assertEqual(X().f(), 'A')
    try:

        class _metaclass(type):

            def mro(self):
                return [self, dict, object]

        class X(object, metaclass=_metaclass):
            pass
        x = object.__new__(X)
        x[5] = 6
    except TypeError:
        pass
    else:
        self.fail('devious mro() return not caught')
    try:

        class _metaclass(type):

            def mro(self):
                return [1]

        class X(object, metaclass=_metaclass):
            pass
    except TypeError:
        pass
    else:
        self.fail('non-class mro() return not caught')
    try:

        class _metaclass(type):

            def mro(self):
                return 1

        class X(object, metaclass=_metaclass):
            pass
    except TypeError:
        pass
    else:
        self.fail('non-sequence mro() return not caught')
