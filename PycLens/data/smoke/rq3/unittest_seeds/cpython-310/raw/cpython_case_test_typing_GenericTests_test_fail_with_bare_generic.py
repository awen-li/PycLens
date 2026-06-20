# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_fail_with_bare_generic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')
    with self.assertRaises(TypeError):
        List[Generic]
    with self.assertRaises(TypeError):
        Tuple[Generic[T]]
    with self.assertRaises(TypeError):
        List[typing.Protocol]
