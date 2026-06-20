# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: EndPositionTests_test_multi_line_str

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = dedent('\n            x = """Some multi-line text.\n\n            It goes on starting from same indent."""\n        ').strip()
    assign = ast.parse(s).body[0]
    self._check_end_pos(assign, 3, 40)
    self._check_end_pos(assign.value, 3, 40)
