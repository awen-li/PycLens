# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ConstantTests_test_string_kind

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = ast.parse('"x"', mode='eval').body
    self.assertEqual(c.value, 'x')
    self.assertEqual(c.kind, None)
    c = ast.parse('u"x"', mode='eval').body
    self.assertEqual(c.value, 'x')
    self.assertEqual(c.kind, 'u')
    c = ast.parse('r"x"', mode='eval').body
    self.assertEqual(c.value, 'x')
    self.assertEqual(c.kind, None)
    c = ast.parse('b"x"', mode='eval').body
    self.assertEqual(c.value, b'x')
    self.assertEqual(c.kind, None)
