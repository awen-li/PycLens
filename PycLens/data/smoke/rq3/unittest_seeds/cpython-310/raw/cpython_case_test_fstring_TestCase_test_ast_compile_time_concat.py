# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_ast_compile_time_concat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = ['']
    expr = "x[0] = 'foo' f'{3}'"
    t = ast.parse(expr)
    c = compile(t, '', 'exec')
    exec(c)
    self.assertEqual(x[0], 'foo3')
