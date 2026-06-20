# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_super.py
# case: TestSuper_test_class_methods_still_working

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(A.cm(), (A, 'A'))
    self.assertEqual(A().cm(), (A, 'A'))
    self.assertEqual(G.cm(), (G, 'A'))
    self.assertEqual(G().cm(), (G, 'A'))
