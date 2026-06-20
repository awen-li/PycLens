# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: HamtTest_test_hamt_basics_4

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h = hamt()
    h1 = h.set('key', [])
    h2 = h1.set('key', [])
    self.assertIsNot(h1, h2)
    self.assertEqual(len(h1), 1)
    self.assertEqual(len(h2), 1)
    self.assertIsNot(h1.get('key'), h2.get('key'))
