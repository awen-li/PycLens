# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_var_annot_syntax_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    check_syntax_error(self, 'def f: int')
    check_syntax_error(self, 'x: int: str')
    check_syntax_error(self, 'def f():\n    nonlocal x: int\n')
    check_syntax_error(self, '[x, 0]: int\n')
    check_syntax_error(self, 'f(): int\n')
    check_syntax_error(self, '(x,): int')
    check_syntax_error(self, 'def f():\n    (x, y): int = (1, 2)\n')
    check_syntax_error(self, 'def f():\n    x: int\n    global x\n')
    check_syntax_error(self, 'def f():\n    global x\n    x: int\n')
