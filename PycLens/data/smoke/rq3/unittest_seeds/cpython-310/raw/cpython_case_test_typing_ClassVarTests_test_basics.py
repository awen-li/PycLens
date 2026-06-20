# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ClassVarTests_test_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        ClassVar[1]
    with self.assertRaises(TypeError):
        ClassVar[int, str]
    with self.assertRaises(TypeError):
        ClassVar[int][str]
