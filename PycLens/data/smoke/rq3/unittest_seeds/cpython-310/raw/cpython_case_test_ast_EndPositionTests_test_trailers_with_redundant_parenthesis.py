# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: EndPositionTests_test_trailers_with_redundant_parenthesis

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = (('( ( ( a ) ) ) ( )', 'Call'), ('( ( ( a ) ) ) ( b )', 'Call'), ('( ( ( a ) ) ) [ b ]', 'Subscript'), ('( ( ( a ) ) ) . b', 'Attribute'))
    for (s, t) in tests:
        with self.subTest(s):
            v = ast.parse(s).body[0].value
            self.assertEqual(type(v).__name__, t)
            self._check_content(s, v, s)
            s2 = 'await ' + s
            v = ast.parse(s2).body[0].value.value
            self.assertEqual(type(v).__name__, t)
            self._check_content(s2, v, s)
