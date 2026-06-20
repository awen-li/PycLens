# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_symtable.py
# case: SymtableTest_test_namespaces

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(self.top.lookup('Mine').is_namespace())
    self.assertTrue(self.Mine.lookup('a_method').is_namespace())
    self.assertTrue(self.top.lookup('spam').is_namespace())
    self.assertTrue(self.spam.lookup('internal').is_namespace())
    self.assertTrue(self.top.lookup('namespace_test').is_namespace())
    self.assertFalse(self.spam.lookup('x').is_namespace())
    self.assertTrue(self.top.lookup('spam').get_namespace() is self.spam)
    ns_test = self.top.lookup('namespace_test')
    self.assertEqual(len(ns_test.get_namespaces()), 2)
    self.assertRaises(ValueError, ns_test.get_namespace)
