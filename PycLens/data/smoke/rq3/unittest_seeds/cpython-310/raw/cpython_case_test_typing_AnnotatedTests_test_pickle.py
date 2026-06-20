# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: AnnotatedTests_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    samples = [typing.Any, typing.Union[int, str], typing.Optional[str], Tuple[int, ...], typing.Callable[[str], bytes]]
    for t in samples:
        x = Annotated[t, 'a']
        for prot in range(pickle.HIGHEST_PROTOCOL + 1):
            with self.subTest(protocol=prot, type=t):
                pickled = pickle.dumps(x, prot)
                restored = pickle.loads(pickled)
                self.assertEqual(x, restored)
    global _Annotated_test_G

    class _Annotated_test_G(Generic[T]):
        x = 1
    G = Annotated[_Annotated_test_G[int], 'A decoration']
    G.foo = 42
    G.bar = 'abc'
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        z = pickle.dumps(G, proto)
        x = pickle.loads(z)
        self.assertEqual(x.foo, 42)
        self.assertEqual(x.bar, 'abc')
        self.assertEqual(x.x, 1)
