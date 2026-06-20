# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_fail_with_bare_union

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        List[Union]
    with self.assertRaises(TypeError):
        Tuple[Optional]
    with self.assertRaises(TypeError):
        ClassVar[ClassVar]
    with self.assertRaises(TypeError):
        List[ClassVar[int]]
