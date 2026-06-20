# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: LiteralTests_test_no_isinstance_or_issubclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        isinstance(1, Literal[1])
    with self.assertRaises(TypeError):
        isinstance(int, Literal[1])
    with self.assertRaises(TypeError):
        issubclass(1, Literal[1])
    with self.assertRaises(TypeError):
        issubclass(int, Literal[1])
