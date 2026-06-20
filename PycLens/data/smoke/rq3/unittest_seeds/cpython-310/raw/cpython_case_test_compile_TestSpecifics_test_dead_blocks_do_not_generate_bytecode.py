# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_dead_blocks_do_not_generate_bytecode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def unused_block_if():
        if 0:
            return 42

    def unused_block_while():
        while 0:
            return 42

    def unused_block_if_else():
        if 1:
            return None
        else:
            return 42

    def unused_block_while_else():
        while 1:
            return None
        else:
            return 42
    funcs = [unused_block_if, unused_block_while, unused_block_if_else, unused_block_while_else]
    for func in funcs:
        opcodes = list(dis.get_instructions(func))
        self.assertLessEqual(len(opcodes), 3)
        self.assertEqual('LOAD_CONST', opcodes[-2].opname)
        self.assertEqual(None, opcodes[-2].argval)
        self.assertEqual('RETURN_VALUE', opcodes[-1].opname)
