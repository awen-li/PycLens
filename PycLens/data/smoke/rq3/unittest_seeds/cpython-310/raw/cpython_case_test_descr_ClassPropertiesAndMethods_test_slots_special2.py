# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_slots_special2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Meta(type):

        def __new__(cls, name, bases, namespace, attr):
            self.assertIn(attr, namespace)
            return super().__new__(cls, name, bases, namespace)

    class C1:

        def __init__(self):
            self.b = 42

    class C2(C1, metaclass=Meta, attr='__classcell__'):
        __slots__ = ['__classcell__']

        def __init__(self):
            super().__init__()
    self.assertIsInstance(C2.__dict__['__classcell__'], types.MemberDescriptorType)
    c = C2()
    self.assertEqual(c.b, 42)
    self.assertNotHasAttr(c, '__classcell__')
    c.__classcell__ = 42
    self.assertEqual(c.__classcell__, 42)
    with self.assertRaises(TypeError):

        class C3:
            __classcell__ = 42
            __slots__ = ['__classcell__']

    class Q1(metaclass=Meta, attr='__qualname__'):
        __slots__ = ['__qualname__']
    self.assertEqual(Q1.__qualname__, C1.__qualname__[:-2] + 'Q1')
    self.assertIsInstance(Q1.__dict__['__qualname__'], types.MemberDescriptorType)
    q = Q1()
    self.assertNotHasAttr(q, '__qualname__')
    q.__qualname__ = 'q'
    self.assertEqual(q.__qualname__, 'q')
    with self.assertRaises(TypeError):

        class Q2:
            __qualname__ = object()
            __slots__ = ['__qualname__']
