# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: AST_Tests_test_ast_validation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    snippets_to_validate = exec_tests + single_tests + eval_tests
    for snippet in snippets_to_validate:
        tree = ast.parse(snippet)
        compile(tree, '<string>', 'exec')
