# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_collections_protocols_allowed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @runtime_checkable
    class Custom(collections.abc.Iterable, Protocol):

        def close(self):
            ...

    class A:
        pass

    class B:

        def __iter__(self):
            return []

        def close(self):
            return 0
    self.assertIsSubclass(B, Custom)
    self.assertNotIsSubclass(A, Custom)
