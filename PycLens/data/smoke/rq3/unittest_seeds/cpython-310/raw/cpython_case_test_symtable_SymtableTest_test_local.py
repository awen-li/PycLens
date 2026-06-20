# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_symtable.py
# case: SymtableTest_test_local

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(self.spam.lookup('x').is_local())
    self.assertFalse(self.spam.lookup('bar').is_local())
    self.assertTrue(self.top.lookup('some_non_assigned_global_var').is_local())
    self.assertTrue(self.top.lookup('some_assigned_global_var').is_local())
