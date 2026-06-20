# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: SimpleNamespaceTests_test_recursive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns1 = types.SimpleNamespace(c='cookie')
    ns2 = types.SimpleNamespace()
    ns3 = types.SimpleNamespace(x=1)
    ns1.spam = ns1
    ns2.spam = ns3
    ns3.spam = ns2
    self.assertEqual(ns1.spam, ns1)
    self.assertEqual(ns1.spam.spam, ns1)
    self.assertEqual(ns1.spam.spam, ns1.spam)
    self.assertEqual(ns2.spam, ns3)
    self.assertEqual(ns3.spam, ns2)
    self.assertEqual(ns2.spam.spam, ns2)
