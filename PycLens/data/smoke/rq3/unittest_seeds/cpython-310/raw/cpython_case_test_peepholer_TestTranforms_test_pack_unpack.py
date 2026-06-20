# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_peepholer.py
# case: TestTranforms_test_pack_unpack

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (line, elem) in (('a, = a,', 'LOAD_CONST'), ('a, b = a, b', 'ROT_TWO'), ('a, b, c = a, b, c', 'ROT_THREE')):
        code = compile(line, '', 'single')
        self.assertInBytecode(code, elem)
        self.assertNotInBytecode(code, 'BUILD_TUPLE')
        self.assertNotInBytecode(code, 'UNPACK_TUPLE')
        self.check_lnotab(code)
