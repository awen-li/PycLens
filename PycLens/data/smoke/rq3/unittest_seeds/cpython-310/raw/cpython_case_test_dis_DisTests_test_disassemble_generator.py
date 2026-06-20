# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dis.py
# case: DisTests_test_disassemble_generator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    gen_func_disas = self.get_disassembly(_g)
    gen_disas = self.get_disassembly(_g(1))
    self.assertEqual(gen_disas, gen_func_disas)
