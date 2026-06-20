# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_protocols_isinstance_properties_and_descriptors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:

        @property
        def attr(self):
            return 42

    class CustomDescriptor:

        def __get__(self, obj, objtype=None):
            return 42

    class D:
        attr = CustomDescriptor()

    class E(C):
        ...

    class F(D):
        ...

    class Empty:
        ...
    T = TypeVar('T')

    @runtime_checkable
    class P(Protocol):

        @property
        def attr(self):
            ...

    @runtime_checkable
    class P1(Protocol):
        attr: int

    @runtime_checkable
    class PG(Protocol[T]):

        @property
        def attr(self):
            ...

    @runtime_checkable
    class PG1(Protocol[T]):
        attr: T
    for protocol_class in (P, P1, PG, PG1):
        for klass in (C, D, E, F):
            with self.subTest(klass=klass.__name__, protocol_class=protocol_class.__name__):
                self.assertIsInstance(klass(), protocol_class)
        with self.subTest(klass='Empty', protocol_class=protocol_class.__name__):
            self.assertNotIsInstance(Empty(), protocol_class)

    class BadP(Protocol):

        @property
        def attr(self):
            ...

    class BadP1(Protocol):
        attr: int

    class BadPG(Protocol[T]):

        @property
        def attr(self):
            ...

    class BadPG1(Protocol[T]):
        attr: T
    for obj in (PG[T], PG[C], PG1[T], PG1[C], BadP, BadP1, BadPG, BadPG1):
        for klass in (C, D, E, F, Empty):
            with self.subTest(klass=klass.__name__, obj=obj):
                with self.assertRaises(TypeError):
                    isinstance(klass(), obj)
