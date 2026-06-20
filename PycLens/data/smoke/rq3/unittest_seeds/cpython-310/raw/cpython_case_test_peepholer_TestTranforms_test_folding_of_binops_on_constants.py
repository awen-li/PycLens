# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_peepholer.py
# case: TestTranforms_test_folding_of_binops_on_constants

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (line, elem) in (('a = 2+3+4', 9), ('"@"*4', '@@@@'), ('a="abc" + "def"', 'abcdef'), ('a = 3**4', 81), ('a = 3*4', 12), ('a = 13//4', 3), ('a = 14%4', 2), ('a = 2+3', 5), ('a = 13-4', 9), ('a = (12,13)[1]', 13), ('a = 13 << 2', 52), ('a = 13 >> 2', 3), ('a = 13 & 7', 5), ('a = 13 ^ 7', 10), ('a = 13 | 7', 15)):
        code = compile(line, '', 'single')
        self.assertInBytecode(code, 'LOAD_CONST', elem)
        for instr in dis.get_instructions(code):
            self.assertFalse(instr.opname.startswith('BINARY_'))
        self.check_lnotab(code)
    code = compile('a=2+"b"', '', 'single')
    self.assertInBytecode(code, 'LOAD_CONST', 2)
    self.assertInBytecode(code, 'LOAD_CONST', 'b')
    self.check_lnotab(code)
    code = compile('a="x"*10000', '', 'single')
    self.assertInBytecode(code, 'LOAD_CONST', 10000)
    self.assertNotIn('x' * 10000, code.co_consts)
    self.check_lnotab(code)
    code = compile('a=1<<1000', '', 'single')
    self.assertInBytecode(code, 'LOAD_CONST', 1000)
    self.assertNotIn(1 << 1000, code.co_consts)
    self.check_lnotab(code)
    code = compile('a=2**1000', '', 'single')
    self.assertInBytecode(code, 'LOAD_CONST', 1000)
    self.assertNotIn(2 ** 1000, code.co_consts)
    self.check_lnotab(code)
