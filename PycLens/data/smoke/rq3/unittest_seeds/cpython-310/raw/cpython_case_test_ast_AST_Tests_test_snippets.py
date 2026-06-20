# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: AST_Tests_test_snippets

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (input, output, kind) in ((exec_tests, exec_results, 'exec'), (single_tests, single_results, 'single'), (eval_tests, eval_results, 'eval')):
        for (i, o) in zip(input, output):
            with self.subTest(action='parsing', input=i):
                ast_tree = compile(i, '?', kind, ast.PyCF_ONLY_AST)
                self.assertEqual(to_tuple(ast_tree), o)
                self._assertTrueorder(ast_tree, (0, 0))
            with self.subTest(action='compiling', input=i, kind=kind):
                compile(ast_tree, '?', kind)
