# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_everything_implements_empty_protocol

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @runtime_checkable
    class Empty(Protocol):
        pass

    class C:
        pass

    def f():
        pass
    for thing in (object, type, tuple, C, types.FunctionType):
        self.assertIsSubclass(thing, Empty)
    for thing in (object(), 1, (), typing, f):
        self.assertIsInstance(thing, Empty)
