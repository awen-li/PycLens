# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: SimpleNamespaceTests_test_unbound

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns1 = vars(types.SimpleNamespace())
    ns2 = vars(types.SimpleNamespace(x=1, y=2))
    self.assertEqual(ns1, {})
    self.assertEqual(ns2, {'y': 2, 'x': 1})
