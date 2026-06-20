# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: EndPositionTests_test_displays

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s1 = '[{}, {1, }, {1, 2,} ]'
    s2 = '{a: b, f (): g () ,}'
    c1 = self._parse_value(s1)
    c2 = self._parse_value(s2)
    self._check_content(s1, c1.elts[0], '{}')
    self._check_content(s1, c1.elts[1], '{1, }')
    self._check_content(s1, c1.elts[2], '{1, 2,}')
    self._check_content(s2, c2.keys[1], 'f ()')
    self._check_content(s2, c2.values[1], 'g ()')
