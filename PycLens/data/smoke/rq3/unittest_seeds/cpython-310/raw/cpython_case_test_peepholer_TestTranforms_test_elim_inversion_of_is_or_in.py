# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_peepholer.py
# case: TestTranforms_test_elim_inversion_of_is_or_in

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (line, cmp_op, invert) in (('not a is b', 'IS_OP', 1), ('not a is not b', 'IS_OP', 0), ('not a in b', 'CONTAINS_OP', 1), ('not a not in b', 'CONTAINS_OP', 0)):
        code = compile(line, '', 'single')
        self.assertInBytecode(code, cmp_op, invert)
        self.check_lnotab(code)
