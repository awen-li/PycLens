# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: AnnotatedTests_test_subst

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dec = 'a decoration'
    dec2 = 'another decoration'
    S = Annotated[T, dec2]
    self.assertEqual(S[int], Annotated[int, dec2])
    self.assertEqual(S[Annotated[int, dec]], Annotated[int, dec, dec2])
    L = Annotated[List[T], dec]
    self.assertEqual(L[int], Annotated[List[int], dec])
    with self.assertRaises(TypeError):
        L[int, int]
    self.assertEqual(S[L[int]], Annotated[List[int], dec, dec2])
    D = Annotated[typing.Dict[KT, VT], dec]
    self.assertEqual(D[str, int], Annotated[typing.Dict[str, int], dec])
    with self.assertRaises(TypeError):
        D[int]
    It = Annotated[int, dec]
    with self.assertRaises(TypeError):
        It[None]
    LI = L[int]
    with self.assertRaises(TypeError):
        LI[None]
