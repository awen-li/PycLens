# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ModuleStateTests_test_subinterpreter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = dedent("\n            import _ast\n            import ast\n            import gc\n            import sys\n            import types\n\n            # Create _ast.AST subclasses instances and call PyAST_Check()\n            ast_tree = compile('x+1', '<string>', 'eval',\n                               flags=ast.PyCF_ONLY_AST)\n            code = compile(ast_tree, 'string', 'eval')\n            if not isinstance(code, types.CodeType):\n                raise AssertionError\n\n            # Unloading the _ast module must not crash.\n            del ast, _ast\n            del sys.modules['ast'], sys.modules['_ast']\n            gc.collect()\n        ")
    res = support.run_in_subinterp(code)
    self.assertEqual(res, 0)
