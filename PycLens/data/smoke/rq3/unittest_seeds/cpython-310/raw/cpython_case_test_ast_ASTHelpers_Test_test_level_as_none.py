# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTHelpers_Test_test_level_as_none

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    body = [ast.ImportFrom(module='time', names=[ast.alias(name='sleep', lineno=0, col_offset=0)], level=None, lineno=0, col_offset=0)]
    mod = ast.Module(body, [])
    code = compile(mod, 'test', 'exec')
    ns = {}
    exec(code, ns)
    self.assertIn('sleep', ns)
