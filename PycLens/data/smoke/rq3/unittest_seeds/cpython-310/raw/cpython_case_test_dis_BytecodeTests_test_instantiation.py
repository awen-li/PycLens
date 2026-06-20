# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dis.py
# case: BytecodeTests_test_instantiation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for obj in [_f, _C(1).__init__, 'a=1', _f.__code__]:
        with self.subTest(obj=obj):
            b = dis.Bytecode(obj)
            self.assertIsInstance(b.codeobj, types.CodeType)
    self.assertRaises(TypeError, dis.Bytecode, object())
