# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: SimpleNamespaceTests_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns1 = types.SimpleNamespace(x=1, y=2, w=3)
    ns2 = types.SimpleNamespace()
    ns2.x = 'spam'
    ns2._y = 5
    name = 'namespace'
    self.assertEqual(repr(ns1), '{name}(x=1, y=2, w=3)'.format(name=name))
    self.assertEqual(repr(ns2), "{name}(x='spam', _y=5)".format(name=name))
