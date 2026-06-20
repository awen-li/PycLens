# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: EndPositionTests_test_import_from_multi_line

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = dedent('\n            from x.y.z import (\n                a, b, c as c\n            )\n        ').strip()
    imp = ast.parse(s).body[0]
    self._check_end_pos(imp, 3, 1)
    self._check_end_pos(imp.names[2], 2, 16)
