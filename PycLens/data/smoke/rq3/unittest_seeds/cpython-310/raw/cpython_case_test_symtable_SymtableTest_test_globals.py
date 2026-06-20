# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_symtable.py
# case: SymtableTest_test_globals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(self.spam.lookup('glob').is_global())
    self.assertFalse(self.spam.lookup('glob').is_declared_global())
    self.assertTrue(self.spam.lookup('bar').is_global())
    self.assertTrue(self.spam.lookup('bar').is_declared_global())
    self.assertFalse(self.internal.lookup('x').is_global())
    self.assertFalse(self.Mine.lookup('instance_var').is_global())
    self.assertTrue(self.spam.lookup('bar').is_global())
    self.assertTrue(self.top.lookup('some_non_assigned_global_var').is_global())
    self.assertTrue(self.top.lookup('some_assigned_global_var').is_global())
