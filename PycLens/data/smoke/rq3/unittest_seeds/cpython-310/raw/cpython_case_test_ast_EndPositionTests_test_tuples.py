# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: EndPositionTests_test_tuples

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s1 = 'x = () ;'
    s2 = 'x = 1 , ;'
    s3 = 'x = (1 , 2 ) ;'
    sm = dedent('\n            x = (\n                a, b,\n            )\n        ').strip()
    (t1, t2, t3, tm) = map(self._parse_value, (s1, s2, s3, sm))
    self._check_content(s1, t1, '()')
    self._check_content(s2, t2, '1 ,')
    self._check_content(s3, t3, '(1 , 2 )')
    self._check_end_pos(tm, 3, 1)
