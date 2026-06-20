# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: EndPositionTests_test_source_segment_missing_info

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = 'v = 1\r\nw = 1\nx = 1\n\ry = 1\r\n'
    (v, w, x, y) = ast.parse(s).body
    del v.lineno
    del w.end_lineno
    del x.col_offset
    del y.end_col_offset
    self.assertIsNone(ast.get_source_segment(s, v))
    self.assertIsNone(ast.get_source_segment(s, w))
    self.assertIsNone(ast.get_source_segment(s, x))
    self.assertIsNone(ast.get_source_segment(s, y))
