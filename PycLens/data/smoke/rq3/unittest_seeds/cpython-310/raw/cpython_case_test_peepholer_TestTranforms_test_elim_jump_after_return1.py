# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_peepholer.py
# case: TestTranforms_test_elim_jump_after_return1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(cond1, cond2):
        if cond1:
            return 1
        if cond2:
            return 2
        while 1:
            return 3
        while 1:
            if cond1:
                return 4
            return 5
        return 6
    self.assertNotInBytecode(f, 'JUMP_FORWARD')
    self.assertNotInBytecode(f, 'JUMP_ABSOLUTE')
    returns = [instr for instr in dis.get_instructions(f) if instr.opname == 'RETURN_VALUE']
    self.assertLessEqual(len(returns), 6)
    self.check_lnotab(f)
