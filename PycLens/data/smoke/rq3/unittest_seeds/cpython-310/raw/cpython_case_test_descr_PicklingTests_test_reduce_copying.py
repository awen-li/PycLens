# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: PicklingTests_test_reduce_copying

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    global C1

    class C1:
        """The state of this class is copyable via its instance dict."""
        ARGS = (1, 2)
        NEED_DICT_COPYING = True

        def __init__(self, a, b):
            super().__init__()
            self.a = a
            self.b = b

        def __repr__(self):
            return 'C1(%r, %r)' % (self.a, self.b)
    global C2

    class C2(list):
        """A list subclass copyable via __getnewargs__."""
        ARGS = (1, 2)
        NEED_DICT_COPYING = False

        def __new__(cls, a, b):
            self = super().__new__(cls)
            self.a = a
            self.b = b
            return self

        def __init__(self, *args):
            super().__init__()
            self.append('cheese')

        @classmethod
        def __getnewargs__(cls):
            return cls.ARGS

        def __repr__(self):
            return 'C2(%r, %r)<%r>' % (self.a, self.b, list(self))
    global C3

    class C3(list):
        """A list subclass copyable via __getstate__."""
        ARGS = (1, 2)
        NEED_DICT_COPYING = False

        def __init__(self, a, b):
            self.a = a
            self.b = b
            self.append('cheese')

        @classmethod
        def __getstate__(cls):
            return cls.ARGS

        def __setstate__(self, state):
            (a, b) = state
            self.a = a
            self.b = b

        def __repr__(self):
            return 'C3(%r, %r)<%r>' % (self.a, self.b, list(self))
    global C4

    class C4(int):
        """An int subclass copyable via __getnewargs__."""
        ARGS = ('hello', 'world', 1)
        NEED_DICT_COPYING = False

        def __new__(cls, a, b, value):
            self = super().__new__(cls, value)
            self.a = a
            self.b = b
            return self

        @classmethod
        def __getnewargs__(cls):
            return cls.ARGS

        def __repr__(self):
            return 'C4(%r, %r)<%r>' % (self.a, self.b, int(self))
    global C5

    class C5(int):
        """An int subclass copyable via __getnewargs_ex__."""
        ARGS = (1, 2)
        KWARGS = {'value': 3}
        NEED_DICT_COPYING = False

        def __new__(cls, a, b, *, value=0):
            self = super().__new__(cls, value)
            self.a = a
            self.b = b
            return self

        @classmethod
        def __getnewargs_ex__(cls):
            return (cls.ARGS, cls.KWARGS)

        def __repr__(self):
            return 'C5(%r, %r)<%r>' % (self.a, self.b, int(self))
    test_classes = (C1, C2, C3, C4, C5)
    pickle_copiers = self._generate_pickle_copiers()
    for (cls, pickle_copier) in itertools.product(test_classes, pickle_copiers):
        with self.subTest(cls=cls, pickle_copier=pickle_copier):
            kwargs = getattr(cls, 'KWARGS', {})
            obj = cls(*cls.ARGS, **kwargs)
            proto = pickle_copier.proto
            objcopy = pickle_copier.copy(obj)
            self._assert_is_copy(obj, objcopy)
            if proto >= 2 and (not cls.NEED_DICT_COPYING):
                objcopy.__dict__.clear()
                objcopy2 = pickle_copier.copy(objcopy)
                self._assert_is_copy(obj, objcopy2)
    for cls in test_classes:
        with self.subTest(cls=cls):
            kwargs = getattr(cls, 'KWARGS', {})
            obj = cls(*cls.ARGS, **kwargs)
            objcopy = deepcopy(obj)
            self._assert_is_copy(obj, objcopy)
            if not cls.NEED_DICT_COPYING:
                objcopy.__dict__.clear()
                objcopy2 = deepcopy(objcopy)
                self._assert_is_copy(obj, objcopy2)
