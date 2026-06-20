# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: EndPositionTests_test_source_segment_tabs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = dedent('\n            class C:\n              \t\x0c  def fun(self) -> None:\n              \t\x0c      pass\n        ').strip()
    s_method = '  \t\x0c  def fun(self) -> None:\n  \t\x0c      pass'
    cdef = ast.parse(s).body[0]
    self.assertEqual(ast.get_source_segment(s, cdef.body[0], padded=True), s_method)
