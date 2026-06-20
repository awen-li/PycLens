# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_protocols_pickleable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    global P, CP
    T = TypeVar('T')

    @runtime_checkable
    class P(Protocol[T]):
        x = 1

    class CP(P[int]):
        pass
    c = CP()
    c.foo = 42
    c.bar = 'abc'
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        z = pickle.dumps(c, proto)
        x = pickle.loads(z)
        self.assertEqual(x.foo, 42)
        self.assertEqual(x.bar, 'abc')
        self.assertEqual(x.x, 1)
        self.assertEqual(x.__dict__, {'foo': 42, 'bar': 'abc'})
        s = pickle.dumps(P, proto)
        D = pickle.loads(s)

        class E:
            x = 1
        self.assertIsInstance(E(), D)
