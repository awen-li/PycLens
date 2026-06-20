# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: SimpleNamespaceTests_test_equal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns1 = types.SimpleNamespace(x=1)
    ns2 = types.SimpleNamespace()
    ns2.x = 1
    self.assertEqual(types.SimpleNamespace(), types.SimpleNamespace())
    self.assertEqual(ns1, ns2)
    self.assertNotEqual(ns2, types.SimpleNamespace())
