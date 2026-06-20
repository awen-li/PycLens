# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dtrace.py
# case: TraceTests_test_verify_call_opcodes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    opcodes = set(['CALL_FUNCTION', 'CALL_FUNCTION_EX', 'CALL_FUNCTION_KW'])
    with open(abspath('call_stack.py')) as f:
        code_string = f.read()

    def get_function_instructions(funcname):
        code = compile(source=code_string, filename='<string>', mode='exec', optimize=self.optimize_python)
        for c in code.co_consts:
            if isinstance(c, types.CodeType) and c.co_name == funcname:
                return dis.get_instructions(c)
        return []
    for instruction in get_function_instructions('start'):
        opcodes.discard(instruction.opname)
    self.assertEqual(set(), opcodes)
