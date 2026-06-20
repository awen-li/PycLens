# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: EndPositionTests_test_redundant_parenthesis

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = '( ( ( a + b ) ) )'
    v = ast.parse(s).body[0].value
    self.assertEqual(type(v).__name__, 'BinOp')
    self._check_content(s, v, 'a + b')
    s2 = 'await ' + s
    v = ast.parse(s2).body[0].value.value
    self.assertEqual(type(v).__name__, 'BinOp')
    self._check_content(s2, v, 'a + b')
