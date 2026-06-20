# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: EndPositionTests_test_continued_str

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = dedent('\n            x = "first part" \\\n            "second part"\n        ').strip()
    assign = ast.parse(s).body[0]
    self._check_end_pos(assign, 2, 13)
    self._check_end_pos(assign.value, 2, 13)
