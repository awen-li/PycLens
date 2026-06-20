# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_super.py
# case: TestSuper_test_unbound_method_transfer_working

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(F().f(), 'ABCD')
    self.assertEqual(F.f(F()), 'ABCD')
