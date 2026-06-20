# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_peepholer.py
# case: TestTranforms_test_folding_of_tuples_of_constants

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (line, elem) in (('a = 1,2,3', (1, 2, 3)), ('("a","b","c")', ('a', 'b', 'c')), ('a,b,c = 1,2,3', (1, 2, 3)), ('(None, 1, None)', (None, 1, None)), ('((1, 2), 3, 4)', ((1, 2), 3, 4))):
        code = compile(line, '', 'single')
        self.assertInBytecode(code, 'LOAD_CONST', elem)
        self.assertNotInBytecode(code, 'BUILD_TUPLE')
        self.check_lnotab(code)
    code = compile(repr(tuple(range(10000))), '', 'single')
    self.assertNotInBytecode(code, 'BUILD_TUPLE')
    load_consts = [instr for instr in dis.get_instructions(code) if instr.opname == 'LOAD_CONST']
    self.assertEqual(len(load_consts), 2)
    self.check_lnotab(code)

    def crater():
        (~[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],)
    self.check_lnotab(crater)
