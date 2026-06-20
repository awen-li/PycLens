# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dis.py
# case: TestDisTraceback_test_distb_explicit_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tb = get_tb()
    self.assertEqual(self.get_disassembly(tb), dis_traceback)
