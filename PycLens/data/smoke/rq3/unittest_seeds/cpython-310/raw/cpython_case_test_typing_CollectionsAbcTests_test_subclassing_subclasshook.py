# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: CollectionsAbcTests_test_subclassing_subclasshook

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Base(typing.Iterable):

        @classmethod
        def __subclasshook__(cls, other):
            if other.__name__ == 'Foo':
                return True
            else:
                return False

    class C(Base):
        ...

    class Foo:
        ...

    class Bar:
        ...
    self.assertIsSubclass(Foo, Base)
    self.assertIsSubclass(Foo, C)
    self.assertNotIsSubclass(Bar, C)
