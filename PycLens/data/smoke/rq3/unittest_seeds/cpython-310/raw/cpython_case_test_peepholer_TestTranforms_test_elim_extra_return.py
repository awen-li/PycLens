# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_peepholer.py
# case: TestTranforms_test_elim_extra_return

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(x):
        return x
    self.assertNotInBytecode(f, 'LOAD_CONST', None)
    returns = [instr for instr in dis.get_instructions(f) if instr.opname == 'RETURN_VALUE']
    self.assertEqual(len(returns), 1)
    self.check_lnotab(f)
