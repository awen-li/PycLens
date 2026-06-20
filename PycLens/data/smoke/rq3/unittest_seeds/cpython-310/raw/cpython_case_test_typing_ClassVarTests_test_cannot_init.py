# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ClassVarTests_test_cannot_init

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        ClassVar()
    with self.assertRaises(TypeError):
        type(ClassVar)()
    with self.assertRaises(TypeError):
        type(ClassVar[Optional[int]])()
