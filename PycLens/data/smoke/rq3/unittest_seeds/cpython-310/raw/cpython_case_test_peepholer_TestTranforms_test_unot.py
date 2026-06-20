# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_peepholer.py
# case: TestTranforms_test_unot

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def unot(x):
        if not x == 2:
            del x
    self.assertNotInBytecode(unot, 'UNARY_NOT')
    self.assertNotInBytecode(unot, 'POP_JUMP_IF_FALSE')
    self.assertInBytecode(unot, 'POP_JUMP_IF_TRUE')
    self.check_lnotab(unot)
