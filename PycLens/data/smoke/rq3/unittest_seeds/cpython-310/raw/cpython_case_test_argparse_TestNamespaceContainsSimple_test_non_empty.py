# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestNamespaceContainsSimple_test_non_empty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns = argparse.Namespace(x=1, y=2)
    self.assertNotIn('', ns)
    self.assertIn('x', ns)
    self.assertIn('y', ns)
    self.assertNotIn('xx', ns)
    self.assertNotIn('z', ns)
