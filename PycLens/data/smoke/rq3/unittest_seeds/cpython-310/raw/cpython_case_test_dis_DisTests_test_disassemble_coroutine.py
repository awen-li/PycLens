# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dis.py
# case: DisTests_test_disassemble_coroutine

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    coro_func_disas = self.get_disassembly(_co)
    coro = _co(1)
    coro.close()
    coro_disas = self.get_disassembly(coro)
    self.assertEqual(coro_disas, coro_func_disas)
