# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestNamespace_test_equality

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns1 = argparse.Namespace(a=1, b=2)
    ns2 = argparse.Namespace(b=2, a=1)
    ns3 = argparse.Namespace(a=1)
    ns4 = argparse.Namespace(b=2)
    self.assertEqual(ns1, ns2)
    self.assertNotEqual(ns1, ns3)
    self.assertNotEqual(ns1, ns4)
    self.assertNotEqual(ns2, ns3)
    self.assertNotEqual(ns2, ns4)
    self.assertTrue(ns1 != ns3)
    self.assertTrue(ns1 != ns4)
    self.assertTrue(ns2 != ns3)
    self.assertTrue(ns2 != ns4)
