# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_multiple_inheritance_special

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    S = TypeVar('S')

    class B(Generic[S]):
        ...

    class C(List[int], B):
        ...
    self.assertEqual(C.__mro__, (C, list, B, Generic, object))
