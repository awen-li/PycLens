# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_parameterized_slots

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')

    class C(Generic[T]):
        __slots__ = ('potato',)
    c = C()
    c_int = C[int]()
    c.potato = 0
    c_int.potato = 0
    with self.assertRaises(AttributeError):
        c.tomato = 0
    with self.assertRaises(AttributeError):
        c_int.tomato = 0

    def foo(x: C['C']):
        ...
    self.assertEqual(get_type_hints(foo, globals(), locals())['x'], C[C])
    self.assertEqual(copy(C[int]), deepcopy(C[int]))
