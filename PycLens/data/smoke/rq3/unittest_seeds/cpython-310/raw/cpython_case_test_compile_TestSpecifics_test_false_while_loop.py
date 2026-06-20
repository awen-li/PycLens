# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_false_while_loop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def break_in_while():
        while False:
            break

    def continue_in_while():
        while False:
            continue
    funcs = [break_in_while, continue_in_while]
    for func in funcs:
        opcodes = list(dis.get_instructions(func))
        self.assertEqual(2, len(opcodes))
        self.assertEqual('LOAD_CONST', opcodes[0].opname)
        self.assertEqual(None, opcodes[0].argval)
        self.assertEqual('RETURN_VALUE', opcodes[1].opname)
