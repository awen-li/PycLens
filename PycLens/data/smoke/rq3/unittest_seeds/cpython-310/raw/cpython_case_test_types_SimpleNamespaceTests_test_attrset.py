# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: SimpleNamespaceTests_test_attrset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns1 = types.SimpleNamespace()
    ns2 = types.SimpleNamespace(x=1, y=2, w=3)
    ns1.a = 'spam'
    ns1.b = 'ham'
    ns2.z = 4
    ns2.theta = None
    self.assertEqual(ns1.__dict__, dict(a='spam', b='ham'))
    self.assertEqual(ns2.__dict__, dict(x=1, y=2, w=3, z=4, theta=None))
