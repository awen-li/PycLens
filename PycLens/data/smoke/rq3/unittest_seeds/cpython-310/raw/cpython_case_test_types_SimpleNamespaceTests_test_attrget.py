# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: SimpleNamespaceTests_test_attrget

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns = types.SimpleNamespace(x=1, y=2, w=3)
    self.assertEqual(ns.x, 1)
    self.assertEqual(ns.y, 2)
    self.assertEqual(ns.w, 3)
    with self.assertRaises(AttributeError):
        ns.z
