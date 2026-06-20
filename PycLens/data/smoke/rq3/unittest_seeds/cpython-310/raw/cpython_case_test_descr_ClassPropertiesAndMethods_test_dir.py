# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    junk = 12
    self.assertEqual(dir(), ['junk', 'self'])
    del junk
    for arg in (2, 2, 2j, 2.0, [2], '2', b'2', (2,), {2: 2}, type, self.test_dir):
        dir(arg)

    def interesting(strings):
        return [s for s in strings if not s.startswith('_')]

    class C(object):
        Cdata = 1

        def Cmethod(self):
            pass
    cstuff = ['Cdata', 'Cmethod']
    self.assertEqual(interesting(dir(C)), cstuff)
    c = C()
    self.assertEqual(interesting(dir(c)), cstuff)
    c.cdata = 2
    c.cmethod = lambda self: 0
    self.assertEqual(interesting(dir(c)), cstuff + ['cdata', 'cmethod'])

    class A(C):
        Adata = 1

        def Amethod(self):
            pass
    astuff = ['Adata', 'Amethod'] + cstuff
    self.assertEqual(interesting(dir(A)), astuff)
    a = A()
    self.assertEqual(interesting(dir(a)), astuff)
    a.adata = 42
    a.amethod = lambda self: 3
    self.assertEqual(interesting(dir(a)), astuff + ['adata', 'amethod'])

    class M(type(sys)):
        pass
    minstance = M('m')
    minstance.b = 2
    minstance.a = 1
    default_attributes = ['__name__', '__doc__', '__package__', '__loader__', '__spec__']
    names = [x for x in dir(minstance) if x not in default_attributes]
    self.assertEqual(names, ['a', 'b'])

    class M2(M):

        def getdict(self):
            return 'Not a dict!'
        __dict__ = property(getdict)
    m2instance = M2('m2')
    m2instance.b = 2
    m2instance.a = 1
    self.assertEqual(m2instance.__dict__, 'Not a dict!')
    with self.assertRaises(TypeError):
        dir(m2instance)
    self.assertEqual(dir(object()), dir(Ellipsis))

    class Wrapper(object):

        def __init__(self, obj):
            self.__obj = obj

        def __repr__(self):
            return 'Wrapper(%s)' % repr(self.__obj)

        def __getitem__(self, key):
            return Wrapper(self.__obj[key])

        def __len__(self):
            return len(self.__obj)

        def __getattr__(self, name):
            return Wrapper(getattr(self.__obj, name))

    class C(object):

        def __getclass(self):
            return Wrapper(type(self))
        __class__ = property(__getclass)
    dir(C())
