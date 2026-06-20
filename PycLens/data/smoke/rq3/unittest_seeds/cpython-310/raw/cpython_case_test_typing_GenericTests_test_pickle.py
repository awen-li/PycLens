# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    global C
    T = TypeVar('T')

    class B(Generic[T]):
        pass

    class C(B[int]):
        pass
    c = C()
    c.foo = 42
    c.bar = 'abc'
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        z = pickle.dumps(c, proto)
        x = pickle.loads(z)
        self.assertEqual(x.foo, 42)
        self.assertEqual(x.bar, 'abc')
        self.assertEqual(x.__dict__, {'foo': 42, 'bar': 'abc'})
    samples = [Any, Union, Tuple, Callable, ClassVar, Union[int, str], ClassVar[List], Tuple[int, ...], Tuple[()], Callable[[str], bytes], typing.DefaultDict, typing.FrozenSet[int]]
    for s in samples:
        for proto in range(pickle.HIGHEST_PROTOCOL + 1):
            z = pickle.dumps(s, proto)
            x = pickle.loads(z)
            self.assertEqual(s, x)
    more_samples = [List, typing.Iterable, typing.Type, List[int], typing.Type[typing.Mapping], typing.AbstractSet[Tuple[int, str]]]
    for s in more_samples:
        for proto in range(pickle.HIGHEST_PROTOCOL + 1):
            z = pickle.dumps(s, proto)
            x = pickle.loads(z)
            self.assertEqual(s, x)
