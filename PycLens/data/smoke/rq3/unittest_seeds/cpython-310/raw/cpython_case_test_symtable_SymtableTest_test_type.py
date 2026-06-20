# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_symtable.py
# case: SymtableTest_test_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.top.get_type(), 'module')
    self.assertEqual(self.Mine.get_type(), 'class')
    self.assertEqual(self.a_method.get_type(), 'function')
    self.assertEqual(self.spam.get_type(), 'function')
    self.assertEqual(self.internal.get_type(), 'function')
