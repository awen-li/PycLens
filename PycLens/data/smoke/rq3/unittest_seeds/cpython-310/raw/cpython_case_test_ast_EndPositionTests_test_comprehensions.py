# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: EndPositionTests_test_comprehensions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = dedent('\n            x = [{x for x, y in stuff\n                  if cond.x} for stuff in things]\n        ').strip()
    cmp = self._parse_value(s)
    self._check_end_pos(cmp, 2, 37)
    self._check_content(s, cmp.generators[0].iter, 'things')
    self._check_content(s, cmp.elt.generators[0].iter, 'stuff')
    self._check_content(s, cmp.elt.generators[0].ifs[0], 'cond.x')
    self._check_content(s, cmp.elt.generators[0].target, 'x, y')
