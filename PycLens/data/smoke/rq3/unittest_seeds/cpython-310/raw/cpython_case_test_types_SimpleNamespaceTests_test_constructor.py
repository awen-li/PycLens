# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: SimpleNamespaceTests_test_constructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns1 = types.SimpleNamespace()
    ns2 = types.SimpleNamespace(x=1, y=2)
    ns3 = types.SimpleNamespace(**dict(x=1, y=2))
    with self.assertRaises(TypeError):
        types.SimpleNamespace(1, 2, 3)
    with self.assertRaises(TypeError):
        types.SimpleNamespace(**{1: 2})
    self.assertEqual(len(ns1.__dict__), 0)
    self.assertEqual(vars(ns1), {})
    self.assertEqual(len(ns2.__dict__), 2)
    self.assertEqual(vars(ns2), {'y': 2, 'x': 1})
    self.assertEqual(len(ns3.__dict__), 2)
    self.assertEqual(vars(ns3), {'y': 2, 'x': 1})
