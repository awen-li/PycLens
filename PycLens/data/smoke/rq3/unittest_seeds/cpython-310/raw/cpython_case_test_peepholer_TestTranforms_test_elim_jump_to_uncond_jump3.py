# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_peepholer.py
# case: TestTranforms_test_elim_jump_to_uncond_jump3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(a, b, c):
        return (a and b) and c
    self.check_jump_targets(f)
    self.check_lnotab(f)
    self.assertEqual(count_instr_recursively(f, 'JUMP_IF_FALSE_OR_POP'), 2)

    def f(a, b, c):
        return (a or b) or c
    self.check_jump_targets(f)
    self.check_lnotab(f)
    self.assertEqual(count_instr_recursively(f, 'JUMP_IF_TRUE_OR_POP'), 2)

    def f(a, b, c):
        return a and b or c
    self.check_jump_targets(f)
    self.check_lnotab(f)
    self.assertNotInBytecode(f, 'JUMP_IF_FALSE_OR_POP')
    self.assertInBytecode(f, 'JUMP_IF_TRUE_OR_POP')
    self.assertInBytecode(f, 'POP_JUMP_IF_FALSE')

    def f(a, b, c):
        return (a or b) and c
    self.check_jump_targets(f)
    self.check_lnotab(f)
    self.assertNotInBytecode(f, 'JUMP_IF_TRUE_OR_POP')
    self.assertInBytecode(f, 'JUMP_IF_FALSE_OR_POP')
    self.assertInBytecode(f, 'POP_JUMP_IF_TRUE')
