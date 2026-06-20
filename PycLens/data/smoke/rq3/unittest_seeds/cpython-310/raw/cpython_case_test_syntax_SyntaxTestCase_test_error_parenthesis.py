# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_syntax.py
# case: SyntaxTestCase_test_error_parenthesis

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for paren in '([{':
        self._check_error(paren + '1 + 2', f"\\{paren}' was never closed")
    for paren in '([{':
        self._check_error(f'a = {paren} 1, 2, 3\nb=3', f"\\{paren}' was never closed")
    for paren in ')]}':
        self._check_error(paren + '1 + 2', f"unmatched '\\{paren}'")
    code = 'func(\n    a=["unclosed], # Need a quote in this comment: "\n    b=2,\n)\n'
    self._check_error(code, "parenthesis '\\)' does not match opening parenthesis '\\['")
