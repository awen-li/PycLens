# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: EndPositionTests_test_binop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = dedent('\n            (1 * 2 + (3 ) +\n                 4\n            )\n        ').strip()
    binop = self._parse_value(s)
    self._check_end_pos(binop, 2, 6)
    self._check_content(s, binop.right, '4')
    self._check_content(s, binop.left, '1 * 2 + (3 )')
    self._check_content(s, binop.left.right, '3')
