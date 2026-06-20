# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_new_repr_bare

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')
    self.assertEqual(repr(Generic[T]), 'typing.Generic[~T]')
    self.assertEqual(repr(typing.Protocol[T]), 'typing.Protocol[~T]')

    class C(typing.Dict[Any, Any]):
        ...
    repr(C.__mro__)
