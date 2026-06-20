# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: AST_Tests_test_field_attr_existence

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (name, item) in ast.__dict__.items():
        if self._is_ast_node(name, item):
            if name == 'Index':
                continue
            x = item()
            if isinstance(x, ast.AST):
                self.assertEqual(type(x._fields), tuple)
