# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_supers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(object):

        def meth(self, a):
            return 'A(%r)' % a
    self.assertEqual(A().meth(1), 'A(1)')

    class B(A):

        def __init__(self):
            self.__super = super(B, self)

        def meth(self, a):
            return 'B(%r)' % a + self.__super.meth(a)
    self.assertEqual(B().meth(2), 'B(2)A(2)')

    class C(A):

        def meth(self, a):
            return 'C(%r)' % a + self.__super.meth(a)
    C._C__super = super(C)
    self.assertEqual(C().meth(3), 'C(3)A(3)')

    class D(C, B):

        def meth(self, a):
            return 'D(%r)' % a + super(D, self).meth(a)
    self.assertEqual(D().meth(4), 'D(4)C(4)B(4)A(4)')

    class mysuper(super):

        def __init__(self, *args):
            return super(mysuper, self).__init__(*args)

    class E(D):

        def meth(self, a):
            return 'E(%r)' % a + mysuper(E, self).meth(a)
    self.assertEqual(E().meth(5), 'E(5)D(5)C(5)B(5)A(5)')

    class F(E):

        def meth(self, a):
            s = self.__super
            return 'F(%r)[%s]' % (a, s.__class__.__name__) + s.meth(a)
    F._F__super = mysuper(F)
    self.assertEqual(F().meth(6), 'F(6)[mysuper]E(6)D(6)C(6)B(6)A(6)')
    try:
        super(D, 42)
    except TypeError:
        pass
    else:
        self.fail("shouldn't allow super(D, 42)")
    try:
        super(D, C())
    except TypeError:
        pass
    else:
        self.fail("shouldn't allow super(D, C())")
    try:
        super(D).__get__(12)
    except TypeError:
        pass
    else:
        self.fail("shouldn't allow super(D).__get__(12)")
    try:
        super(D).__get__(C())
    except TypeError:
        pass
    else:
        self.fail("shouldn't allow super(D).__get__(C())")

    class DDbase(object):

        def getx(self):
            return 42
        x = property(getx)

    class DDsub(DDbase):

        def getx(self):
            return 'hello'
        x = property(getx)
    dd = DDsub()
    self.assertEqual(dd.x, 'hello')
    self.assertEqual(super(DDsub, dd).x, 42)

    class Base(object):
        aProp = property(lambda self: 'foo')

    class Sub(Base):

        @classmethod
        def test(klass):
            return super(Sub, klass).aProp
    self.assertEqual(Sub.test(), Base.aProp)
    with self.assertRaises(TypeError):
        super(Base, kw=1)
