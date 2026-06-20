# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTHelpers_Test_test_dump_indent

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    node = ast.parse('spam(eggs, "and cheese")')
    self.assertEqual(ast.dump(node, indent=3), "Module(\n   body=[\n      Expr(\n         value=Call(\n            func=Name(id='spam', ctx=Load()),\n            args=[\n               Name(id='eggs', ctx=Load()),\n               Constant(value='and cheese')],\n            keywords=[]))],\n   type_ignores=[])")
    self.assertEqual(ast.dump(node, annotate_fields=False, indent='\t'), "Module(\n\t[\n\t\tExpr(\n\t\t\tCall(\n\t\t\t\tName('spam', Load()),\n\t\t\t\t[\n\t\t\t\t\tName('eggs', Load()),\n\t\t\t\t\tConstant('and cheese')],\n\t\t\t\t[]))],\n\t[])")
    self.assertEqual(ast.dump(node, include_attributes=True, indent=3), "Module(\n   body=[\n      Expr(\n         value=Call(\n            func=Name(\n               id='spam',\n               ctx=Load(),\n               lineno=1,\n               col_offset=0,\n               end_lineno=1,\n               end_col_offset=4),\n            args=[\n               Name(\n                  id='eggs',\n                  ctx=Load(),\n                  lineno=1,\n                  col_offset=5,\n                  end_lineno=1,\n                  end_col_offset=9),\n               Constant(\n                  value='and cheese',\n                  lineno=1,\n                  col_offset=11,\n                  end_lineno=1,\n                  end_col_offset=23)],\n            keywords=[],\n            lineno=1,\n            col_offset=0,\n            end_lineno=1,\n            end_col_offset=24),\n         lineno=1,\n         col_offset=0,\n         end_lineno=1,\n         end_col_offset=24)],\n   type_ignores=[])")
