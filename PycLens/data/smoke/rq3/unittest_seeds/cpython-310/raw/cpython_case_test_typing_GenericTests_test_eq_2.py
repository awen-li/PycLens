# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_eq_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(Generic[T]):
        pass

    class B(Generic[T]):
        pass
    self.assertEqual(A, A)
    self.assertNotEqual(A, B)
    self.assertEqual(A[T], A[T])
    self.assertNotEqual(A[T], B[T])
