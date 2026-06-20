# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_diamond_inheritance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(object):

        def spam(self):
            return 'A'
    self.assertEqual(A().spam(), 'A')

    class B(A):

        def boo(self):
            return 'B'

        def spam(self):
            return 'B'
    self.assertEqual(B().spam(), 'B')
    self.assertEqual(B().boo(), 'B')

    class C(A):

        def boo(self):
            return 'C'
    self.assertEqual(C().spam(), 'A')
    self.assertEqual(C().boo(), 'C')

    class D(B, C):
        pass
    self.assertEqual(D().spam(), 'B')
    self.assertEqual(D().boo(), 'B')
    self.assertEqual(D.__mro__, (D, B, C, A, object))

    class E(C, B):
        pass
    self.assertEqual(E().spam(), 'B')
    self.assertEqual(E().boo(), 'C')
    self.assertEqual(E.__mro__, (E, C, B, A, object))
    try:

        class F(D, E):
            pass
    except TypeError:
        pass
    else:
        self.fail('expected MRO order disagreement (F)')
    try:

        class G(E, D):
            pass
    except TypeError:
        pass
    else:
        self.fail('expected MRO order disagreement (G)')
