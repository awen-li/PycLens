# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_subscripted_generics_as_proxies

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')

    class C(Generic[T]):
        x = 'def'
    self.assertEqual(C[int].x, 'def')
    self.assertEqual(C[C[int]].x, 'def')
    C[C[int]].x = 'changed'
    self.assertEqual(C.x, 'changed')
    self.assertEqual(C[str].x, 'changed')
    C[List[str]].z = 'new'
    self.assertEqual(C.z, 'new')
    self.assertEqual(C[Tuple[int]].z, 'new')
    self.assertEqual(C().x, 'changed')
    self.assertEqual(C[Tuple[str]]().z, 'new')

    class D(C[T]):
        pass
    self.assertEqual(D[int].x, 'changed')
    self.assertEqual(D.z, 'new')
    D.z = 'from derived z'
    D[int].x = 'from derived x'
    self.assertEqual(C.x, 'changed')
    self.assertEqual(C[int].z, 'new')
    self.assertEqual(D.x, 'from derived x')
    self.assertEqual(D[str].z, 'from derived z')
