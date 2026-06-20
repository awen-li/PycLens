# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: EndPositionTests_test_slices

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s1 = 'f()[1, 2] [0]'
    s2 = 'x[ a.b: c.d]'
    sm = dedent('\n            x[ a.b: f () ,\n               g () : c.d\n              ]\n        ').strip()
    (i1, i2, im) = map(self._parse_value, (s1, s2, sm))
    self._check_content(s1, i1.value, 'f()[1, 2]')
    self._check_content(s1, i1.value.slice, '1, 2')
    self._check_content(s2, i2.slice.lower, 'a.b')
    self._check_content(s2, i2.slice.upper, 'c.d')
    self._check_content(sm, im.slice.elts[0].upper, 'f ()')
    self._check_content(sm, im.slice.elts[1].lower, 'g ()')
    self._check_end_pos(im, 3, 3)
