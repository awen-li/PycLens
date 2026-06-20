# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__opcode.py
# case: OpcodeTests_test_stack_effect

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(stack_effect(dis.opmap['POP_TOP']), -1)
    self.assertEqual(stack_effect(dis.opmap['DUP_TOP_TWO']), 2)
    self.assertEqual(stack_effect(dis.opmap['BUILD_SLICE'], 0), -1)
    self.assertEqual(stack_effect(dis.opmap['BUILD_SLICE'], 1), -1)
    self.assertEqual(stack_effect(dis.opmap['BUILD_SLICE'], 3), -2)
    self.assertRaises(ValueError, stack_effect, 30000)
    self.assertRaises(ValueError, stack_effect, dis.opmap['BUILD_SLICE'])
    self.assertRaises(ValueError, stack_effect, dis.opmap['POP_TOP'], 0)
    for (name, code) in dis.opmap.items():
        with self.subTest(opname=name):
            if code < dis.HAVE_ARGUMENT:
                stack_effect(code)
                self.assertRaises(ValueError, stack_effect, code, 0)
            else:
                stack_effect(code, 0)
                self.assertRaises(ValueError, stack_effect, code)
    for code in set(range(256)) - set(dis.opmap.values()):
        with self.subTest(opcode=code):
            self.assertRaises(ValueError, stack_effect, code)
            self.assertRaises(ValueError, stack_effect, code, 0)
