# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: CollectionsAbcTests_test_no_generator_instantiation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        typing.Generator()
    with self.assertRaises(TypeError):
        typing.Generator[T, T, T]()
    with self.assertRaises(TypeError):
        typing.Generator[int, int, int]()
