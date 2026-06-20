# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_subclass_right_op

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class B(int):

        def __floordiv__(self, other):
            return 'B.__floordiv__'

        def __rfloordiv__(self, other):
            return 'B.__rfloordiv__'
    self.assertEqual(B(1) // 1, 'B.__floordiv__')
    self.assertEqual(1 // B(1), 'B.__rfloordiv__')

    class C(object):

        def __floordiv__(self, other):
            return 'C.__floordiv__'

        def __rfloordiv__(self, other):
            return 'C.__rfloordiv__'
    self.assertEqual(C() // 1, 'C.__floordiv__')
    self.assertEqual(1 // C(), 'C.__rfloordiv__')

    class D(C):

        def __floordiv__(self, other):
            return 'D.__floordiv__'

        def __rfloordiv__(self, other):
            return 'D.__rfloordiv__'
    self.assertEqual(D() // C(), 'D.__floordiv__')
    self.assertEqual(C() // D(), 'D.__rfloordiv__')

    class E(C):
        pass
    self.assertEqual(E.__rfloordiv__, C.__rfloordiv__)
    self.assertEqual(E() // 1, 'C.__floordiv__')
    self.assertEqual(1 // E(), 'C.__rfloordiv__')
    self.assertEqual(E() // C(), 'C.__floordiv__')
    self.assertEqual(C() // E(), 'C.__floordiv__')
