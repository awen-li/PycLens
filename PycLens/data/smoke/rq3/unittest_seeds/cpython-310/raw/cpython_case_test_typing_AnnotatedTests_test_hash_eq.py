# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: AnnotatedTests_test_hash_eq

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(len({Annotated[int, 4, 5], Annotated[int, 4, 5]}), 1)
    self.assertNotEqual(Annotated[int, 4, 5], Annotated[int, 5, 4])
    self.assertNotEqual(Annotated[int, 4, 5], Annotated[str, 4, 5])
    self.assertNotEqual(Annotated[int, 4], Annotated[int, 4, 4])
    self.assertEqual({Annotated[int, 4, 5], Annotated[int, 4, 5], Annotated[T, 4, 5]}, {Annotated[int, 4, 5], Annotated[T, 4, 5]})
