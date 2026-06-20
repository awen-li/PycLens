# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_generic_hashes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(Generic[T]):
        ...

    class B(Generic[T]):

        class A(Generic[T]):
            ...
    self.assertEqual(A, A)
    self.assertEqual(mod_generics_cache.A[str], mod_generics_cache.A[str])
    self.assertEqual(B.A, B.A)
    self.assertEqual(mod_generics_cache.B.A[B.A[str]], mod_generics_cache.B.A[B.A[str]])
    self.assertNotEqual(A, B.A)
    self.assertNotEqual(A, mod_generics_cache.A)
    self.assertNotEqual(A, mod_generics_cache.B.A)
    self.assertNotEqual(B.A, mod_generics_cache.A)
    self.assertNotEqual(B.A, mod_generics_cache.B.A)
    self.assertNotEqual(A[str], B.A[str])
    self.assertNotEqual(A[List[Any]], B.A[List[Any]])
    self.assertNotEqual(A[str], mod_generics_cache.A[str])
    self.assertNotEqual(A[str], mod_generics_cache.B.A[str])
    self.assertNotEqual(B.A[int], mod_generics_cache.A[int])
    self.assertNotEqual(B.A[List[Any]], mod_generics_cache.B.A[List[Any]])
    self.assertNotEqual(Tuple[A[str]], Tuple[B.A[str]])
    self.assertNotEqual(Tuple[A[List[Any]]], Tuple[B.A[List[Any]]])
    self.assertNotEqual(Union[str, A[str]], Union[str, mod_generics_cache.A[str]])
    self.assertNotEqual(Union[A[str], A[str]], Union[A[str], mod_generics_cache.A[str]])
    self.assertNotEqual(typing.FrozenSet[A[str]], typing.FrozenSet[mod_generics_cache.B.A[str]])
    if sys.version_info[:2] > (3, 2):
        self.assertTrue(repr(Tuple[A[str]]).endswith('<locals>.A[str]]'))
        self.assertTrue(repr(Tuple[B.A[str]]).endswith('<locals>.B.A[str]]'))
        self.assertTrue(repr(Tuple[mod_generics_cache.A[str]]).endswith('mod_generics_cache.A[str]]'))
        self.assertTrue(repr(Tuple[mod_generics_cache.B.A[str]]).endswith('mod_generics_cache.B.A[str]]'))
