# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTHelpers_Test_test_iter_fields

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    node = ast.parse('foo()', mode='eval')
    d = dict(ast.iter_fields(node.body))
    self.assertEqual(d.pop('func').id, 'foo')
    self.assertEqual(d, {'keywords': [], 'args': []})
