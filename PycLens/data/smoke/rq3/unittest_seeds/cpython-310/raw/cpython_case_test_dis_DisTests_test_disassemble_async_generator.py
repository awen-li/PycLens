# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dis.py
# case: DisTests_test_disassemble_async_generator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    agen_func_disas = self.get_disassembly(_ag)
    agen_disas = self.get_disassembly(_ag(1))
    self.assertEqual(agen_disas, agen_func_disas)
