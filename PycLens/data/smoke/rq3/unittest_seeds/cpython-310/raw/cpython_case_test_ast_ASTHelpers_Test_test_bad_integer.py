# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTHelpers_Test_test_bad_integer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    body = [ast.ImportFrom(module='time', names=[ast.alias(name='sleep')], level=None, lineno=None, col_offset=None)]
    mod = ast.Module(body, [])
    with self.assertRaises(ValueError) as cm:
        compile(mod, 'test', 'exec')
    self.assertIn('invalid integer value: None', str(cm.exception))
