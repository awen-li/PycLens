# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_redundant_jump_in_if_else_break

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def if_else_break():
        val = 1
        while True:
            if val > 0:
                val -= 1
            else:
                break
            val = -1
    INSTR_SIZE = 2
    HANDLED_JUMPS = ('POP_JUMP_IF_FALSE', 'POP_JUMP_IF_TRUE', 'JUMP_ABSOLUTE', 'JUMP_FORWARD')
    for (line, instr) in enumerate(dis.Bytecode(if_else_break)):
        if instr.opname == 'JUMP_FORWARD':
            self.assertNotEqual(instr.arg, 0)
        elif instr.opname in HANDLED_JUMPS:
            self.assertNotEqual(instr.arg, (line + 1) * INSTR_SIZE)
