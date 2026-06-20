# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_symtable.py
# case: SymtableTest_test_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.top.get_name(), 'top')
    self.assertEqual(self.spam.get_name(), 'spam')
    self.assertEqual(self.spam.lookup('x').get_name(), 'x')
    self.assertEqual(self.Mine.get_name(), 'Mine')
