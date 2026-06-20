# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: SimpleNamespaceTests_test_underlying_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns1 = types.SimpleNamespace()
    ns2 = types.SimpleNamespace(x=1, y=2)
    ns3 = types.SimpleNamespace(a=True, b=False)
    mapping = ns3.__dict__
    del ns3
    self.assertEqual(ns1.__dict__, {})
    self.assertEqual(ns2.__dict__, {'y': 2, 'x': 1})
    self.assertEqual(mapping, dict(a=True, b=False))
