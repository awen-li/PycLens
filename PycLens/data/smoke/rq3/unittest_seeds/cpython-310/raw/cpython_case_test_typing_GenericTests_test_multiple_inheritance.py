# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_multiple_inheritance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(Generic[T, VT]):
        pass

    class B(Generic[KT, T]):
        pass

    class C(A[T, VT], Generic[VT, T, KT], B[KT, T]):
        pass
    self.assertEqual(C.__parameters__, (VT, T, KT))
