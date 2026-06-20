# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: EndPositionTests_test_class_def

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = dedent('\n            class C(A, B):\n                x: int = 0\n        ').strip()
    cdef = ast.parse(s).body[0]
    self._check_end_pos(cdef, 2, 14)
    self._check_content(s, cdef.bases[1], 'B')
    self._check_content(s, cdef.body[0], 'x: int = 0')
