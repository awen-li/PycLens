# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dis.py
# case: BytecodeTests_test_from_traceback

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tb = get_tb()
    b = dis.Bytecode.from_traceback(tb)
    while tb.tb_next:
        tb = tb.tb_next
    self.assertEqual(b.current_offset, tb.tb_lasti)
