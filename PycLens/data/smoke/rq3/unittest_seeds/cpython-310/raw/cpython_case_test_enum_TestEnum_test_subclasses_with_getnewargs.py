# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_subclasses_with_getnewargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class NamedInt(int):
        __qualname__ = 'NamedInt'

        def __new__(cls, *args):
            _args = args
            (name, *args) = args
            if len(args) == 0:
                raise TypeError('name and value must be specified')
            self = int.__new__(cls, *args)
            self._intname = name
            self._args = _args
            return self

        def __getnewargs__(self):
            return self._args

        @property
        def __name__(self):
            return self._intname

        def __repr__(self):
            return '{}({!r}, {})'.format(type(self).__name__, self.__name__, int.__repr__(self))

        def __str__(self):
            base = int
            base_str = base.__str__
            if base_str.__objclass__ is object:
                return base.__repr__(self)
            return base_str(self)

        def __add__(self, other):
            temp = int(self) + int(other)
            if isinstance(self, NamedInt) and isinstance(other, NamedInt):
                return NamedInt('({0} + {1})'.format(self.__name__, other.__name__), temp)
            else:
                return temp

    class NEI(NamedInt, Enum):
        __qualname__ = 'NEI'
        x = ('the-x', 1)
        y = ('the-y', 2)
    self.assertIs(NEI.__new__, Enum.__new__)
    self.assertEqual(repr(NEI.x + NEI.y), "NamedInt('(the-x + the-y)', 3)")
    globals()['NamedInt'] = NamedInt
    globals()['NEI'] = NEI
    NI5 = NamedInt('test', 5)
    self.assertEqual(NI5, 5)
    test_pickle_dump_load(self.assertEqual, NI5, 5)
    self.assertEqual(NEI.y.value, 2)
    test_pickle_dump_load(self.assertIs, NEI.y)
    test_pickle_dump_load(self.assertIs, NEI)
