# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_metaclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(metaclass=type):

        def __init__(self):
            self.__state = 0

        def getstate(self):
            return self.__state

        def setstate(self, state):
            self.__state = state
    a = C()
    self.assertEqual(a.getstate(), 0)
    a.setstate(10)
    self.assertEqual(a.getstate(), 10)

    class _metaclass(type):

        def myself(cls):
            return cls

    class D(metaclass=_metaclass):
        pass
    self.assertEqual(D.myself(), D)
    d = D()
    self.assertEqual(d.__class__, D)

    class M1(type):

        def __new__(cls, name, bases, dict):
            dict['__spam__'] = 1
            return type.__new__(cls, name, bases, dict)

    class C(metaclass=M1):
        pass
    self.assertEqual(C.__spam__, 1)
    c = C()
    self.assertEqual(c.__spam__, 1)

    class _instance(object):
        pass

    class M2(object):

        @staticmethod
        def __new__(cls, name, bases, dict):
            self = object.__new__(cls)
            self.name = name
            self.bases = bases
            self.dict = dict
            return self

        def __call__(self):
            it = _instance()
            for key in self.dict:
                if key.startswith('__'):
                    continue
                setattr(it, key, self.dict[key].__get__(it, self))
            return it

    class C(metaclass=M2):

        def spam(self):
            return 42
    self.assertEqual(C.name, 'C')
    self.assertEqual(C.bases, ())
    self.assertIn('spam', C.dict)
    c = C()
    self.assertEqual(c.spam(), 42)

    class autosuper(type):

        def __new__(metaclass, name, bases, dict):
            cls = super(autosuper, metaclass).__new__(metaclass, name, bases, dict)
            while name[:1] == '_':
                name = name[1:]
            if name:
                name = '_%s__super' % name
            else:
                name = '__super'
            setattr(cls, name, super(cls))
            return cls

    class A(metaclass=autosuper):

        def meth(self):
            return 'A'

    class B(A):

        def meth(self):
            return 'B' + self.__super.meth()

    class C(A):

        def meth(self):
            return 'C' + self.__super.meth()

    class D(C, B):

        def meth(self):
            return 'D' + self.__super.meth()
    self.assertEqual(D().meth(), 'DCBA')

    class E(B, C):

        def meth(self):
            return 'E' + self.__super.meth()
    self.assertEqual(E().meth(), 'EBCA')

    class autoproperty(type):

        def __new__(metaclass, name, bases, dict):
            hits = {}
            for (key, val) in dict.items():
                if key.startswith('_get_'):
                    key = key[5:]
                    (get, set) = hits.get(key, (None, None))
                    get = val
                    hits[key] = (get, set)
                elif key.startswith('_set_'):
                    key = key[5:]
                    (get, set) = hits.get(key, (None, None))
                    set = val
                    hits[key] = (get, set)
            for (key, (get, set)) in hits.items():
                dict[key] = property(get, set)
            return super(autoproperty, metaclass).__new__(metaclass, name, bases, dict)

    class A(metaclass=autoproperty):

        def _get_x(self):
            return -self.__x

        def _set_x(self, x):
            self.__x = -x
    a = A()
    self.assertNotHasAttr(a, 'x')
    a.x = 12
    self.assertEqual(a.x, 12)
    self.assertEqual(a._A__x, -12)

    class multimetaclass(autoproperty, autosuper):
        pass

    class A(metaclass=multimetaclass):

        def _get_x(self):
            return 'A'

    class B(A):

        def _get_x(self):
            return 'B' + self.__super._get_x()

    class C(A):

        def _get_x(self):
            return 'C' + self.__super._get_x()

    class D(C, B):

        def _get_x(self):
            return 'D' + self.__super._get_x()
    self.assertEqual(D().x, 'DCBA')

    class T(type):
        counter = 0

        def __init__(self, *args):
            T.counter += 1

    class C(metaclass=T):
        pass
    self.assertEqual(T.counter, 1)
    a = C()
    self.assertEqual(type(a), C)
    self.assertEqual(T.counter, 1)

    class C(object):
        pass
    c = C()
    try:
        c()
    except TypeError:
        pass
    else:
        self.fail('calling object w/o call method should raise TypeError')

    class A(type):

        def __new__(*args, **kwargs):
            return type.__new__(*args, **kwargs)

    class B(object):
        pass

    class C(object, metaclass=A):
        pass

    class D(B, C):
        pass
    self.assertIs(A, type(D))
    new_calls = []

    class AMeta(type):

        @staticmethod
        def __new__(mcls, name, bases, ns):
            new_calls.append('AMeta')
            return super().__new__(mcls, name, bases, ns)

        @classmethod
        def __prepare__(mcls, name, bases):
            return {}

    class BMeta(AMeta):

        @staticmethod
        def __new__(mcls, name, bases, ns):
            new_calls.append('BMeta')
            return super().__new__(mcls, name, bases, ns)

        @classmethod
        def __prepare__(mcls, name, bases):
            ns = super().__prepare__(name, bases)
            ns['BMeta_was_here'] = True
            return ns

    class A(metaclass=AMeta):
        pass
    self.assertEqual(['AMeta'], new_calls)
    new_calls.clear()

    class B(metaclass=BMeta):
        pass
    self.assertEqual(['BMeta', 'AMeta'], new_calls)
    new_calls.clear()

    class C(A, B):
        pass
    self.assertEqual(['BMeta', 'AMeta'], new_calls)
    new_calls.clear()
    self.assertIn('BMeta_was_here', C.__dict__)

    class C2(B, A):
        pass
    self.assertEqual(['BMeta', 'AMeta'], new_calls)
    new_calls.clear()
    self.assertIn('BMeta_was_here', C2.__dict__)

    class D(C, metaclass=type):
        pass
    self.assertEqual(['BMeta', 'AMeta'], new_calls)
    new_calls.clear()
    self.assertIn('BMeta_was_here', D.__dict__)

    class E(C, metaclass=AMeta):
        pass
    self.assertEqual(['BMeta', 'AMeta'], new_calls)
    new_calls.clear()
    self.assertIn('BMeta_was_here', E.__dict__)
    marker = object()

    def func(*args, **kwargs):
        return marker

    class X(metaclass=func):
        pass

    class Y(object, metaclass=func):
        pass

    class Z(D, metaclass=func):
        pass
    self.assertIs(marker, X)
    self.assertIs(marker, Y)
    self.assertIs(marker, Z)
    prepare_calls = []

    class ANotMeta:

        def __new__(mcls, *args, **kwargs):
            new_calls.append('ANotMeta')
            return super().__new__(mcls)

        @classmethod
        def __prepare__(mcls, name, bases):
            prepare_calls.append('ANotMeta')
            return {}

    class BNotMeta(ANotMeta):

        def __new__(mcls, *args, **kwargs):
            new_calls.append('BNotMeta')
            return super().__new__(mcls)

        @classmethod
        def __prepare__(mcls, name, bases):
            prepare_calls.append('BNotMeta')
            return super().__prepare__(name, bases)

    class A(metaclass=ANotMeta):
        pass
    self.assertIs(ANotMeta, type(A))
    self.assertEqual(['ANotMeta'], prepare_calls)
    prepare_calls.clear()
    self.assertEqual(['ANotMeta'], new_calls)
    new_calls.clear()

    class B(metaclass=BNotMeta):
        pass
    self.assertIs(BNotMeta, type(B))
    self.assertEqual(['BNotMeta', 'ANotMeta'], prepare_calls)
    prepare_calls.clear()
    self.assertEqual(['BNotMeta', 'ANotMeta'], new_calls)
    new_calls.clear()

    class C(A, B):
        pass
    self.assertIs(BNotMeta, type(C))
    self.assertEqual(['BNotMeta', 'ANotMeta'], new_calls)
    new_calls.clear()
    self.assertEqual(['BNotMeta', 'ANotMeta'], prepare_calls)
    prepare_calls.clear()

    class C2(B, A):
        pass
    self.assertIs(BNotMeta, type(C2))
    self.assertEqual(['BNotMeta', 'ANotMeta'], new_calls)
    new_calls.clear()
    self.assertEqual(['BNotMeta', 'ANotMeta'], prepare_calls)
    prepare_calls.clear()
    with self.assertRaises(TypeError):

        class D(C, metaclass=type):
            pass

    class E(C, metaclass=ANotMeta):
        pass
    self.assertIs(BNotMeta, type(E))
    self.assertEqual(['BNotMeta', 'ANotMeta'], new_calls)
    new_calls.clear()
    self.assertEqual(['BNotMeta', 'ANotMeta'], prepare_calls)
    prepare_calls.clear()

    class F(object(), C):
        pass
    self.assertIs(BNotMeta, type(F))
    self.assertEqual(['BNotMeta', 'ANotMeta'], new_calls)
    new_calls.clear()
    self.assertEqual(['BNotMeta', 'ANotMeta'], prepare_calls)
    prepare_calls.clear()

    class F2(C, object()):
        pass
    self.assertIs(BNotMeta, type(F2))
    self.assertEqual(['BNotMeta', 'ANotMeta'], new_calls)
    new_calls.clear()
    self.assertEqual(['BNotMeta', 'ANotMeta'], prepare_calls)
    prepare_calls.clear()
    with self.assertRaises(TypeError):

        class X(C, int()):
            pass
    with self.assertRaises(TypeError):

        class X(int(), C):
            pass
