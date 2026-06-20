# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_peepholer.py
# case: TestTranforms_test_constant_folding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    exprs = ['3 * -5', '-3 * 5', '2 * (3 * 4)', '(2 * 3) * 4', '(-1, 2, 3)', '(1, -2, 3)', '(1, 2, -3)', '(1, 2, -3) * 6', 'lambda x: x in {(3 * -5) + (-1 - 6), (1, -2, 3) * 2, None}']
    for e in exprs:
        code = compile(e, '', 'single')
        for instr in dis.get_instructions(code):
            self.assertFalse(instr.opname.startswith('UNARY_'))
            self.assertFalse(instr.opname.startswith('BINARY_'))
            self.assertFalse(instr.opname.startswith('BUILD_'))
        self.check_lnotab(code)
