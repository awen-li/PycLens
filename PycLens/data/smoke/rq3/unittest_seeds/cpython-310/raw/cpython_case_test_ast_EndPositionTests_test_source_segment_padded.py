# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: EndPositionTests_test_source_segment_padded

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s_orig = dedent('\n            class C:\n                def fun(self) -> None:\n                    "ЖЖЖЖЖ"\n        ').strip()
    s_method = '    def fun(self) -> None:\n        "ЖЖЖЖЖ"'
    cdef = ast.parse(s_orig).body[0]
    self.assertEqual(ast.get_source_segment(s_orig, cdef.body[0], padded=True), s_method)
