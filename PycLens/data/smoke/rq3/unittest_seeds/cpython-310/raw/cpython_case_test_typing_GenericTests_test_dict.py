# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')

    class B(Generic[T]):
        pass
    b = B()
    b.foo = 42
    self.assertEqual(b.__dict__, {'foo': 42})

    class C(B[int]):
        pass
    c = C()
    c.bar = 'abc'
    self.assertEqual(c.__dict__, {'bar': 'abc'})
