# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTHelpers_Test_test_increment_lineno_on_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    src = ast.parse(dedent('        a = 1\n        b = 2 # type: ignore\n        c = 3\n        d = 4 # type: ignore@tag\n        '), type_comments=True)
    ast.increment_lineno(src, n=5)
    self.assertEqual(src.type_ignores[0].lineno, 7)
    self.assertEqual(src.type_ignores[1].lineno, 9)
    self.assertEqual(src.type_ignores[1].tag, '@tag')
