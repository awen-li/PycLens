# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: SimpleNamespaceTests_test_attrdel

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns1 = types.SimpleNamespace()
    ns2 = types.SimpleNamespace(x=1, y=2, w=3)
    with self.assertRaises(AttributeError):
        del ns1.spam
    with self.assertRaises(AttributeError):
        del ns2.spam
    del ns2.y
    self.assertEqual(vars(ns2), dict(w=3, x=1))
    ns2.y = 'spam'
    self.assertEqual(vars(ns2), dict(w=3, x=1, y='spam'))
    del ns2.y
    self.assertEqual(vars(ns2), dict(w=3, x=1))
    ns1.spam = 5
    self.assertEqual(vars(ns1), dict(spam=5))
    del ns1.spam
    self.assertEqual(vars(ns1), {})
