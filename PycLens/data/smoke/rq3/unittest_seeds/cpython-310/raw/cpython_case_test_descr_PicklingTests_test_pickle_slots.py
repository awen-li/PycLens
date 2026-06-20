# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: PicklingTests_test_pickle_slots

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    global C

    class C:
        __slots__ = ['a']
    with self.assertRaises(TypeError):
        pickle.dumps(C(), 0)
    global D

    class D(C):
        pass
    with self.assertRaises(TypeError):
        pickle.dumps(D(), 0)

    class C:
        """A class with __getstate__ and __setstate__ implemented."""
        __slots__ = ['a']

        def __getstate__(self):
            state = getattr(self, '__dict__', {}).copy()
            for cls in type(self).__mro__:
                for slot in cls.__dict__.get('__slots__', ()):
                    try:
                        state[slot] = getattr(self, slot)
                    except AttributeError:
                        pass
            return state

        def __setstate__(self, state):
            for (k, v) in state.items():
                setattr(self, k, v)

        def __repr__(self):
            return '%s()<%r>' % (type(self).__name__, self.__getstate__())

    class D(C):
        """A subclass of a class with slots."""
        pass
    global E

    class E(C):
        """A subclass with an extra slot."""
        __slots__ = ['b']
    for pickle_copier in self._generate_pickle_copiers():
        with self.subTest(pickle_copier=pickle_copier):
            x = C()
            y = pickle_copier.copy(x)
            self._assert_is_copy(x, y)
            x.a = 42
            y = pickle_copier.copy(x)
            self._assert_is_copy(x, y)
            x = D()
            x.a = 42
            x.b = 100
            y = pickle_copier.copy(x)
            self._assert_is_copy(x, y)
            x = E()
            x.a = 42
            x.b = 'foo'
            y = pickle_copier.copy(x)
            self._assert_is_copy(x, y)
