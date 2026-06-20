# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_peepholer.py
# case: TestTranforms_test_while_one

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        while 1:
            pass
        return list
    for elem in ('LOAD_CONST', 'POP_JUMP_IF_FALSE'):
        self.assertNotInBytecode(f, elem)
    for elem in ('JUMP_ABSOLUTE',):
        self.assertInBytecode(f, elem)
    self.check_lnotab(f)
