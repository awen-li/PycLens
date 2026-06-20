# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: EndPositionTests_test_source_segment_endings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = 'v = 1\r\nw = 1\nx = 1\n\ry = 1\rz = 1\r\n'
    (v, w, x, y, z) = ast.parse(s).body
    self._check_content(s, v, 'v = 1')
    self._check_content(s, w, 'w = 1')
    self._check_content(s, x, 'x = 1')
    self._check_content(s, y, 'y = 1')
    self._check_content(s, z, 'z = 1')
