# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: AnnotatedTests_test_specialize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    L = Annotated[List[T], 'my decoration']
    LI = Annotated[List[int], 'my decoration']
    self.assertEqual(L[int], Annotated[List[int], 'my decoration'])
    self.assertEqual(L[int].__metadata__, ('my decoration',))
    self.assertEqual(L[int].__origin__, List[int])
    with self.assertRaises(TypeError):
        LI[int]
    with self.assertRaises(TypeError):
        L[int, float]
