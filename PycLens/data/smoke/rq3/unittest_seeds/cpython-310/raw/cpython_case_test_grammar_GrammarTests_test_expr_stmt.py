# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_expr_stmt

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    1
    (1, 2, 3)
    x = 1
    x = (1, 2, 3)
    x = y = z = (1, 2, 3)
    (x, y, z) = (1, 2, 3)
    abc = (a, b, c) = (x, y, z) = xyz = (1, 2, (3, 4))
    check_syntax_error(self, 'x + 1 = 1')
    check_syntax_error(self, 'a + 1 = b + 2')
