# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_parameterized_slots_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')

    class D(Generic[T]):
        __slots__ = {'banana': 42}
    d = D()
    d_int = D[int]()
    d.banana = 'yes'
    d_int.banana = 'yes'
    with self.assertRaises(AttributeError):
        d.foobar = 'no'
    with self.assertRaises(AttributeError):
        d_int.foobar = 'no'
