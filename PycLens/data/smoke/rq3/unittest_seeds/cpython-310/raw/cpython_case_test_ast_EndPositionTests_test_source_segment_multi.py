# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: EndPositionTests_test_source_segment_multi

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s_orig = dedent('\n            x = (\n                a, b,\n            ) + ()\n        ').strip()
    s_tuple = dedent('\n            (\n                a, b,\n            )\n        ').strip()
    binop = self._parse_value(s_orig)
    self.assertEqual(ast.get_source_segment(s_orig, binop.left), s_tuple)
