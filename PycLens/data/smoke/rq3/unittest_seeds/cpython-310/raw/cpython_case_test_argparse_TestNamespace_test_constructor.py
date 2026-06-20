# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestNamespace_test_constructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns = argparse.Namespace()
    self.assertRaises(AttributeError, getattr, ns, 'x')
    ns = argparse.Namespace(a=42, b='spam')
    self.assertEqual(ns.a, 42)
    self.assertEqual(ns.b, 'spam')
