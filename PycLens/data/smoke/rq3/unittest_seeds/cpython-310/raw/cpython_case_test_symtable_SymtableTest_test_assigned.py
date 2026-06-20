# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_symtable.py
# case: SymtableTest_test_assigned

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(self.spam.lookup('x').is_assigned())
    self.assertTrue(self.spam.lookup('bar').is_assigned())
    self.assertTrue(self.top.lookup('spam').is_assigned())
    self.assertTrue(self.Mine.lookup('a_method').is_assigned())
    self.assertFalse(self.internal.lookup('x').is_assigned())
