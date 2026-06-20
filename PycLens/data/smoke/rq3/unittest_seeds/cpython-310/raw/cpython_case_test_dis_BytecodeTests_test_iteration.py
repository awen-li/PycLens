# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dis.py
# case: BytecodeTests_test_iteration

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for obj in [_f, _C(1).__init__, 'a=1', _f.__code__]:
        with self.subTest(obj=obj):
            via_object = list(dis.Bytecode(obj))
            via_generator = list(dis.get_instructions(obj))
            self.assertEqual(via_object, via_generator)
