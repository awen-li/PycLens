# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__opcode.py
# case: OpcodeTests_test_stack_effect_jump

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    JUMP_IF_TRUE_OR_POP = dis.opmap['JUMP_IF_TRUE_OR_POP']
    self.assertEqual(stack_effect(JUMP_IF_TRUE_OR_POP, 0), 0)
    self.assertEqual(stack_effect(JUMP_IF_TRUE_OR_POP, 0, jump=True), 0)
    self.assertEqual(stack_effect(JUMP_IF_TRUE_OR_POP, 0, jump=False), -1)
    FOR_ITER = dis.opmap['FOR_ITER']
    self.assertEqual(stack_effect(FOR_ITER, 0), 1)
    self.assertEqual(stack_effect(FOR_ITER, 0, jump=True), -1)
    self.assertEqual(stack_effect(FOR_ITER, 0, jump=False), 1)
    JUMP_FORWARD = dis.opmap['JUMP_FORWARD']
    self.assertEqual(stack_effect(JUMP_FORWARD, 0), 0)
    self.assertEqual(stack_effect(JUMP_FORWARD, 0, jump=True), 0)
    self.assertEqual(stack_effect(JUMP_FORWARD, 0, jump=False), 0)
    has_jump = dis.hasjabs + dis.hasjrel
    for (name, code) in dis.opmap.items():
        with self.subTest(opname=name):
            if code < dis.HAVE_ARGUMENT:
                common = stack_effect(code)
                jump = stack_effect(code, jump=True)
                nojump = stack_effect(code, jump=False)
            else:
                common = stack_effect(code, 0)
                jump = stack_effect(code, 0, jump=True)
                nojump = stack_effect(code, 0, jump=False)
            if code in has_jump:
                self.assertEqual(common, max(jump, nojump))
            else:
                self.assertEqual(jump, common)
                self.assertEqual(nojump, common)
