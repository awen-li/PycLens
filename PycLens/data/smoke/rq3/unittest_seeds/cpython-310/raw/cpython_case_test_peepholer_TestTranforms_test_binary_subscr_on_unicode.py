# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_peepholer.py
# case: TestTranforms_test_binary_subscr_on_unicode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = compile('"foo"[0]', '', 'single')
    self.assertInBytecode(code, 'LOAD_CONST', 'f')
    self.assertNotInBytecode(code, 'BINARY_SUBSCR')
    self.check_lnotab(code)
    code = compile('"a\uffff"[1]', '', 'single')
    self.assertInBytecode(code, 'LOAD_CONST', '\uffff')
    self.assertNotInBytecode(code, 'BINARY_SUBSCR')
    self.check_lnotab(code)
    code = compile('"𒍅"[0]', '', 'single')
    self.assertInBytecode(code, 'LOAD_CONST', '𒍅')
    self.assertNotInBytecode(code, 'BINARY_SUBSCR')
    self.check_lnotab(code)
    code = compile('"fuu"[10]', '', 'single')
    self.assertInBytecode(code, 'BINARY_SUBSCR')
    self.check_lnotab(code)
