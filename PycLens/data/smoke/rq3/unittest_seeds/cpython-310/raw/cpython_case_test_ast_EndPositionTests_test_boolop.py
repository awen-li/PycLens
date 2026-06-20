# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: EndPositionTests_test_boolop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = dedent('\n            if (one_condition and\n                    (other_condition or yet_another_one)):\n                pass\n        ').strip()
    bop = ast.parse(s).body[0].test
    self._check_end_pos(bop, 2, 44)
    self._check_content(s, bop.values[1], 'other_condition or yet_another_one')
