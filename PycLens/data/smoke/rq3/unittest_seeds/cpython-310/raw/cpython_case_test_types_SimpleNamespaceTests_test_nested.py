# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: SimpleNamespaceTests_test_nested

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns1 = types.SimpleNamespace(a=1, b=2)
    ns2 = types.SimpleNamespace()
    ns3 = types.SimpleNamespace(x=ns1)
    ns2.spam = ns1
    ns2.ham = '?'
    ns2.spam = ns3
    self.assertEqual(vars(ns1), dict(a=1, b=2))
    self.assertEqual(vars(ns2), dict(spam=ns3, ham='?'))
    self.assertEqual(ns2.spam, ns3)
    self.assertEqual(vars(ns3), dict(x=ns1))
    self.assertEqual(ns3.x.a, 1)
