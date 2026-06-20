# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ConstantTests_test_validation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError) as cm:
        self.compile_constant([1, 2, 3])
    self.assertEqual(str(cm.exception), 'got an invalid type in Constant: list')
