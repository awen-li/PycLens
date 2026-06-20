# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_peepholer.py
# case: TestTranforms_test_folding_of_unaryops_on_constants

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (line, elem) in (('-0.5', -0.5), ('-0.0', -0.0), ('-(1.0-1.0)', -0.0), ('-0', 0), ('~-2', 1), ('+1', 1)):
        code = compile(line, '', 'single')
        self.assertInBytecode(code, 'LOAD_CONST', elem)
        for instr in dis.get_instructions(code):
            self.assertFalse(instr.opname.startswith('UNARY_'))
        self.check_lnotab(code)

    def negzero():
        return -(1.0 - 1.0)
    for instr in dis.get_instructions(negzero):
        self.assertFalse(instr.opname.startswith('UNARY_'))
    self.check_lnotab(negzero)
    for (line, elem, opname) in (('-"abc"', 'abc', 'UNARY_NEGATIVE'), ('~"abc"', 'abc', 'UNARY_INVERT')):
        code = compile(line, '', 'single')
        self.assertInBytecode(code, 'LOAD_CONST', elem)
        self.assertInBytecode(code, opname)
        self.check_lnotab(code)
