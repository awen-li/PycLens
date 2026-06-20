# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dis.py
# case: TestBytecodeTestCase_test_assert_not_in_with_arg_not_in_bytecode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = compile('a = 1', '<string>', 'exec')
    self.assertInBytecode(code, 'LOAD_CONST')
    self.assertInBytecode(code, 'LOAD_CONST', 1)
    self.assertNotInBytecode(code, 'LOAD_CONST', 2)
